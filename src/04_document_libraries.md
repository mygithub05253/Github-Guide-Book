# Part 4: 문서 처리 라이브러리 완전 가이드

> 이 파트는 가이드북의 핵심입니다. 여기서 소개하는 라이브러리들은 이 가이드북 자체를 생성하는 데 실제로 사용되었습니다.
> `scripts/` 디렉토리의 빌드 파이프라인이 바로 이 라이브러리들의 실전 활용 예제입니다.

## 학습 목표
- Python/Java/JavaScript 문서 처리 라이브러리 활용
- Word, Excel, PDF, PowerPoint 자동 생성
- 문서 자동화 파이프라인 구축

---


## 4-1. Python 문서 라이브러리

### 4-1-1. python-docx (Word 문서)

**설치**
```bash
pip install python-docx
```

**핵심 API**
```python
from docx import Document
from docx.shared import Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH

doc = Document()
title = doc.add_heading('프로젝트 리포트', 0)
title.alignment = WD_ALIGN_PARAGRAPH.CENTER
doc.add_paragraph('작성일: 2024-04-06')
doc.add_heading('1. 개요', level=1)
doc.add_paragraph('본문...', style='List Number')

table = doc.add_table(rows=2, cols=2)
table.style = 'Light Grid Accent 1'
table.rows[0].cells[0].text = '날짜'
table.rows[0].cells[1].text = '진행상황'

doc.add_picture('chart.png', width=Inches(5))
doc.save('report.docx')
```

외워둘 것: `add_heading(text, level)`, `add_paragraph(text, style)`, `add_table(rows, cols)`, `add_picture(path, width)`, `save(path)`. 동적 보고서는 dict/list를 순회하며 위 호출을 반복하면 끝입니다.

### 4-1-2. openpyxl (Excel 처리)

**설치**
```bash
pip install openpyxl
```

**핵심 API**
```python
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment

wb = Workbook()
ws = wb.active
ws.title = "Sales"

ws.append(['날짜', '상품', '판매량', '가격', '합계'])
for cell in ws[1]:
    cell.font = Font(bold=True, color="FFFFFF")
    cell.fill = PatternFill("solid", fgColor="4472C4")
    cell.alignment = Alignment(horizontal="center")

ws.append(['2024-01-01', 'A상품', 10, 50000, None])
ws['E2'] = '=C2*D2'               # 수식
ws.column_dimensions['A'].width = 12
wb.save('sales.xlsx')
```

외워둘 것: `ws.append(row)`, `ws[f'E{r}'] = value`, `ws.column_dimensions[...].width`, `Font/PatternFill/Alignment`.

**Excel 읽기 및 분석**
```python
from openpyxl import load_workbook
import statistics

wb = load_workbook('sales.xlsx')
ws = wb.active

# 데이터 읽기
data = []
for row in ws.iter_rows(min_row=2, values_only=True):
    if row[0]:  # 헤더 제외
        data.append(row)

# 분석
sales = [row[4] for row in data]  # 합계 열
print(f"총 판매액: {sum(sales)}")
print(f"평균 판매액: {statistics.mean(sales):.0f}")
print(f"중간값: {statistics.median(sales):.0f}")

# 필터링
high_sales = [row for row in data if row[4] > 500000]
print(f"500,000 이상 거래: {len(high_sales)}건")
```

**피벗 테이블**
```python
from openpyxl import load_workbook
from openpyxl.worksheet.pivot import Pivot

wb = load_workbook('sales.xlsx')
ws = wb.active

# 데이터 범위
pivot = Pivot()
pivot.fromSheet = ws
pivot.ref = f'A1:E{ws.max_row}'

# 피벗 테이블 생성
pivot_sheet = wb.create_sheet('Pivot')
pivot.location = f'{pivot_sheet.title}!A1'

wb.save('sales_pivot.xlsx')
```

### 4-1-3. python-pptx (PowerPoint)

**설치**
```bash
pip install python-pptx
```

**핵심 API**
```python
from pptx import Presentation
from pptx.util import Inches
from pptx.chart.data import CategoryChartData
from pptx.enum.chart import XL_CHART_TYPE

prs = Presentation()

# 제목 슬라이드 (layout 0)
slide = prs.slides.add_slide(prs.slide_layouts[0])
slide.shapes.title.text = "프로젝트 발표"
slide.placeholders[1].text = "2024 Q1"

# 차트 슬라이드 (layout 5 = Blank)
slide = prs.slides.add_slide(prs.slide_layouts[5])
chart_data = CategoryChartData()
chart_data.categories = ['1월', '2월', '3월']
chart_data.add_series('판매액', (100, 120, 150))
slide.shapes.add_chart(XL_CHART_TYPE.COLUMN_CLUSTERED,
                      Inches(1), Inches(1), Inches(8), Inches(5), chart_data)

prs.save('presentation.pptx')
```

외워둘 것: `slide_layouts[0]`(Title), `[1]`(Title+Content), `[5]`(Blank). `add_textbox`, `add_picture`, `add_chart`로 레이아웃을 직접 쌓을 수 있습니다.

### 4-1-4. PyMuPDF (PDF 처리)

**설치**
```bash
pip install PyMuPDF
```

**PDF 읽기 및 추출**
```python
import fitz  # PyMuPDF

# PDF 열기
pdf_document = fitz.open('document.pdf')

# 기본 정보
print(f"페이지 수: {len(pdf_document)}")

# 텍스트 추출
for page_num in range(len(pdf_document)):
    page = pdf_document[page_num]
    text = page.get_text()
    print(f"--- 페이지 {page_num + 1} ---")
    print(text)

# 이미지 추출
for page_num in range(len(pdf_document)):
    page = pdf_document[page_num]
    images = page.get_images()

    for img_index, img in enumerate(images):
        xref = img[0]
        pix = fitz.Pixmap(pdf_document, xref)

        if pix.n - pix.alpha < 4:
            pix.save(f"page{page_num}_img{img_index}.png")
        else:
            pix = fitz.Pixmap(fitz.csRGB, pix)
            pix.save(f"page{page_num}_img{img_index}.png")

pdf_document.close()
```

**PDF 생성**
```python
import fitz

# 새 PDF 생성
doc = fitz.open()

# 페이지 추가
page = doc.new_page()

# 텍스트 추가
page.insert_text((50, 50), "안녕하세요", fontsize=12)

# 사각형 그리기
page.draw_rect((50, 80, 200, 120), color=(0, 0, 1), width=2)

# 이미지 삽입
page.insert_image((50, 150, 300, 350), filename="chart.png")

# 저장
doc.save('generated.pdf')
```

---

## 4-2. Java 문서 라이브러리

### 4-2-1. Apache POI (Excel/Word/PowerPoint)

**Maven 의존성**
```xml
<dependency>
    <groupId>org.apache.poi</groupId>
    <artifactId>poi</artifactId>
    <version>5.2.3</version>
</dependency>
<dependency>
    <groupId>org.apache.poi</groupId>
    <artifactId>poi-ooxml</artifactId>
    <version>5.2.3</version>
</dependency>
```

**Excel 핵심 API (XSSFWorkbook)**
```java
Workbook wb = new XSSFWorkbook();
Sheet sheet = wb.createSheet("Sales");

Row header = sheet.createRow(0);
String[] cols = {"날짜", "상품", "판매량", "가격"};
for (int i = 0; i < cols.length; i++) {
    header.createCell(i).setCellValue(cols[i]);
}

Row row = sheet.createRow(1);
row.createCell(0).setCellValue("2024-01-01");
row.createCell(2).setCellValue(10);

try (FileOutputStream fos = new FileOutputStream("sales.xlsx")) {
    wb.write(fos);
}
wb.close();
```

읽기는 `WorkbookFactory.create(new File(...))` → `sheet.getSheetAt(0)` → `for (Row r : sheet)` 순서. 스타일은 `CellStyle` + `Font` + `FillPatternType.SOLID_FOREGROUND`.

**Word 핵심 API (XWPFDocument)**
```java
XWPFDocument doc = new XWPFDocument();

XWPFParagraph title = doc.createParagraph();
title.setAlignment(ParagraphAlignment.CENTER);
XWPFRun run = title.createRun();
run.setText("프로젝트 리포트");
run.setBold(true);
run.setFontSize(18);

XWPFTable table = doc.createTable(3, 2);
table.getRow(0).getCell(0).setText("날짜");
table.getRow(0).getCell(1).setText("진행상황");

try (FileOutputStream fos = new FileOutputStream("report.docx")) {
    doc.write(fos);
}
doc.close();
```

외워둘 것: 모든 텍스트는 `Paragraph → Run` 2단계로 추가. 스타일은 Run에 걸립니다.

### 4-2-2. iText (PDF 생성/편집)

**Maven 의존성**
```xml
<dependency>
    <groupId>com.itextpdf</groupId>
    <artifactId>itext7-core</artifactId>
    <version>7.2.3</version>
    <type>pom</type>
</dependency>
```

**PDF 생성**
```java
import com.itextpdf.kernel.pdf.PdfDocument;
import com.itextpdf.kernel.pdf.PdfWriter;
import com.itextpdf.layout.Document;
import com.itextpdf.layout.element.Paragraph;
import com.itextpdf.layout.element.Table;
import java.io.IOException;

public class PdfGenerator {
    public static void createPdf() throws IOException {
        String dest = "output.pdf";

        PdfWriter writer = new PdfWriter(dest);
        PdfDocument pdfDoc = new PdfDocument(writer);
        Document document = new Document(pdfDoc);

        // 제목
        document.add(new Paragraph("프로젝트 리포트")
            .setBold()
            .setFontSize(18));

        // 본문
        document.add(new Paragraph("작성일: 2024년 4월 6일"));

        // 테이블
        Table table = new Table(2);
        table.addCell("날짜");
        table.addCell("진행상황");
        table.addCell("2024-01-01");
        table.addCell("기획");
        table.addCell("2024-02-01");
        table.addCell("개발");

        document.add(table);
        document.close();
    }
}
```

---

## 4-3. JavaScript 문서 라이브러리

### 4-3-1. SheetJS (xlsx)

**설치**
```bash
npm install xlsx
```

**기본 사용법**
```javascript
import XLSX from 'xlsx';

// Excel 파일 읽기
const file = input.files[0];
const reader = new FileReader();

reader.onload = (e) => {
    const data = new Uint8Array(e.target.result);
    const workbook = XLSX.read(data, { type: 'array' });
    const worksheet = workbook.Sheets[workbook.SheetNames[0]];
    const json = XLSX.utils.sheet_to_json(worksheet);

    console.log(json);
};

reader.readAsArrayBuffer(file);

// Excel 파일 생성
const data = [
    { 날짜: '2024-01-01', 상품: 'A상품', 판매량: 10 },
    { 날짜: '2024-01-02', 상품: 'B상품', 판매량: 15 },
];

const worksheet = XLSX.utils.json_to_sheet(data);
const workbook = XLSX.utils.book_new();
XLSX.utils.book_append_sheet(workbook, worksheet, "Sales");
XLSX.writeFile(workbook, "sales.xlsx");
```

### 4-3-2. PDFKit

**설치**
```bash
npm install pdfkit
```

**PDF 핵심 API**
```javascript
const PDFDocument = require('pdfkit');
const fs = require('fs');

const doc = new PDFDocument();
doc.pipe(fs.createWriteStream('output.pdf'));

doc.fontSize(25).text('프로젝트 리포트', { align: 'center' });
doc.fontSize(12).text('작성일: 2024-04-06');
doc.image('chart.png', { width: 400 });
doc.addPage().text('두 번째 페이지');

doc.end();
```

외워둘 것: `doc.text()`는 연쇄 호출 가능. 테이블은 좌표 계산(`x + i * width`)으로 직접 그립니다.

### 4-3-3. docx (Word 생성)

**설치**
```bash
npm install docx
```

**Word 핵심 API**
```javascript
import { Document, Packer, Paragraph, Table, TableRow, TableCell } from "docx";
import fs from "fs";

const cell = (text) => new TableCell({ children: [new Paragraph(text)] });

const doc = new Document({
  sections: [{
    children: [
      new Paragraph({ text: "프로젝트 리포트", bold: true, size: 28 }),
      new Paragraph({ text: "작성일: 2024-04-06" }),
      new Table({
        rows: [
          new TableRow({ children: [cell("날짜"), cell("진행상황")] }),
          new TableRow({ children: [cell("2024-01-01"), cell("기획")] }),
        ],
      }),
    ],
  }],
});

Packer.toBuffer(doc).then((buf) => fs.writeFileSync("report.docx", buf));
```

외워둘 것: `Document` → `sections[].children[]`에 `Paragraph`/`Table`을 선언형으로 쌓는 패턴. `Packer.toBuffer()`로 바이너리를 얻어 저장합니다.

---

## 4-4. 문서 자동화 파이프라인

### Claude Code와 문서 라이브러리 통합

**종합 문서 생성 워크플로우**

이 가이드북의 `scripts/build_guidebook.py`가 실제 예시입니다. 구조는 단순합니다.

```python
class DocumentPipeline:
    def __init__(self, data):
        self.data = data

    def generate_all(self):
        self._word()      # python-docx
        self._excel()     # openpyxl
        self._pptx()      # python-pptx
```

각 `_word`, `_excel`, `_pptx` 메서드는 앞서 본 핵심 API를 그대로 호출합니다. 입력을 dict 하나로 통일하면 같은 데이터로 세 포맷이 동시에 나옵니다.

> Claude Code 활용 팁
> `> "내 프로젝트 데이터(dict)를 받아서 docx/xlsx/pptx 3종 문서를 한 번에 생성하는 DocumentPipeline 클래스를 만들어줘"`

---

## 실전 활용: 포트폴리오 자동 생성

GitHub API + python-docx를 결합해 "내 Top 10 레포" 포트폴리오를 자동으로 만드는 스크립트를 작성할 수 있습니다.

```python
import requests
from docx import Document

def generate_portfolio(username):
    repos = requests.get(f'https://api.github.com/users/{username}/repos').json()
    repos = sorted(repos, key=lambda r: r['stargazers_count'], reverse=True)[:10]

    doc = Document()
    doc.add_heading(f'{username} 포트폴리오', 0)
    for repo in repos:
        doc.add_heading(repo['name'], level=1)
        doc.add_paragraph(repo.get('description') or '')
        doc.add_paragraph(f"⭐ {repo['stargazers_count']} | {repo.get('language') or 'N/A'}")
        doc.add_paragraph(repo['html_url'])
    doc.save(f'{username}_portfolio.docx')

generate_portfolio('torvalds')
```

> Claude Code 활용 팁
> `> "위 스크립트를 내 GitHub 아이디로 실행해서 Top 10 레포 포트폴리오를 Word로 뽑아줘. 각 레포마다 README 첫 문단도 요약해서 넣어줘."`

