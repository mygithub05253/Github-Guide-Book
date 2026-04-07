# 4-2. Java 문서 라이브러리

> Spring Boot 백엔드에서 "주간 매출 리포트를 PDF로 다운로드" 같은 기능을 만든다면, Python 대신 **Java 라이브러리로 해결하는 게 정답**이에요. 이 섹션에서는 Apache POI와 iText를 다룹니다.

---

## 4-2-1. Apache POI — Excel/Word/PowerPoint

**한 줄 소개**: **Java 진영의 표준** Microsoft Office 문서 처리 라이브러리. Excel, Word, PowerPoint 모두 지원.

**왜 봐야 하는가**: Spring Boot 프로젝트에서 Excel 다운로드 API를 만들어야 한다면 100% 이 라이브러리를 쓰게 됩니다. 취업 면접에서 "Excel 다운로드 구현해보셨나요?"는 단골 질문이에요.

**난이도**: ⭐⭐⭐

### 📋 배울 수 있는 것

- XSSFWorkbook (xlsx) / HSSFWorkbook (xls) 차이
- Cell, Row, Sheet 계층 구조
- CellStyle, Font, Fill로 스타일링
- 수식, 병합 셀, 차트
- Word(XWPFDocument) 기본 API

### 🚀 15분 퀵스타트

#### Step 1: 의존성 추가

**Maven (`pom.xml`)**:

```xml
<dependency>
    <groupId>org.apache.poi</groupId>
    <artifactId>poi</artifactId>
    <version>5.2.5</version>
</dependency>
<dependency>
    <groupId>org.apache.poi</groupId>
    <artifactId>poi-ooxml</artifactId>
    <version>5.2.5</version>
</dependency>
```

**Gradle (`build.gradle`)**:

```groovy
implementation 'org.apache.poi:poi:5.2.5'
implementation 'org.apache.poi:poi-ooxml:5.2.5'
```

!!! warning "⚠️ 주의"
    `poi`만 넣으면 `.xls`(구버전)만 됩니다. `poi-ooxml`까지 넣어야 `.xlsx`를 다룰 수 있어요. 실무에서 필요한 건 거의 `.xlsx`이므로 **두 개 다 꼭 넣으세요**.

#### Step 2: Excel 파일 생성

```java
import org.apache.poi.ss.usermodel.*;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;
import java.io.FileOutputStream;
import java.io.IOException;

public class ExcelDemo {
    public static void main(String[] args) throws IOException {
        try (Workbook wb = new XSSFWorkbook()) {
            Sheet sheet = wb.createSheet("Sales");

            // 헤더
            Row header = sheet.createRow(0);
            String[] cols = {"날짜", "상품", "수량", "가격"};
            for (int i = 0; i < cols.length; i++) {
                header.createCell(i).setCellValue(cols[i]);
            }

            // 데이터
            Row row = sheet.createRow(1);
            row.createCell(0).setCellValue("2026-04-01");
            row.createCell(1).setCellValue("A상품");
            row.createCell(2).setCellValue(10);
            row.createCell(3).setCellValue(50000);

            try (FileOutputStream fos = new FileOutputStream("sales.xlsx")) {
                wb.write(fos);
            }
        }
        System.out.println("sales.xlsx 생성 완료");
    }
}
```

#### Step 3: 실행

```bash
./gradlew run
# 또는 IDE의 Run 버튼
```

!!! info "예상 출력"
    ```
    sales.xlsx 생성 완료
    ```

#### Step 4: 헤더 스타일 적용

```java
import org.apache.poi.ss.usermodel.*;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;

Workbook wb = new XSSFWorkbook();
Sheet sheet = wb.createSheet("Styled");

// 스타일 생성
CellStyle headerStyle = wb.createCellStyle();
Font headerFont = wb.createFont();
headerFont.setBold(true);
headerFont.setColor(IndexedColors.WHITE.getIndex());
headerStyle.setFont(headerFont);
headerStyle.setFillForegroundColor(IndexedColors.BLUE.getIndex());
headerStyle.setFillPattern(FillPatternType.SOLID_FOREGROUND);
headerStyle.setAlignment(HorizontalAlignment.CENTER);

Row header = sheet.createRow(0);
String[] cols = {"날짜", "상품", "수량", "가격"};
for (int i = 0; i < cols.length; i++) {
    Cell cell = header.createCell(i);
    cell.setCellValue(cols[i]);
    cell.setCellStyle(headerStyle);
}

sheet.setColumnWidth(0, 15 * 256);  // 256 = 한 글자 너비
```

#### Step 5: Excel 파일 읽기

```java
try (Workbook wb = WorkbookFactory.create(new File("sales.xlsx"))) {
    Sheet sheet = wb.getSheetAt(0);
    for (Row row : sheet) {
        for (Cell cell : row) {
            System.out.print(cell + " | ");
        }
        System.out.println();
    }
}
```

### 💡 실전 패턴: Spring Boot에서 Excel 다운로드 API

```java
@RestController
@RequiredArgsConstructor
public class ReportController {

    private final SalesService salesService;

    @GetMapping("/api/reports/sales.xlsx")
    public void downloadSalesReport(HttpServletResponse response) throws IOException {
        List<Sale> sales = salesService.findAll();

        try (Workbook wb = new XSSFWorkbook()) {
            Sheet sheet = wb.createSheet("매출");
            Row header = sheet.createRow(0);
            header.createCell(0).setCellValue("날짜");
            header.createCell(1).setCellValue("상품");
            header.createCell(2).setCellValue("금액");

            int rowNum = 1;
            for (Sale s : sales) {
                Row row = sheet.createRow(rowNum++);
                row.createCell(0).setCellValue(s.getDate().toString());
                row.createCell(1).setCellValue(s.getProduct());
                row.createCell(2).setCellValue(s.getAmount());
            }

            response.setContentType(
                "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            );
            response.setHeader(
                "Content-Disposition", "attachment; filename=sales.xlsx"
            );
            wb.write(response.getOutputStream());
        }
    }
}
```

!!! tip "💡 꿀팁: 취업 포트폴리오 필살기"
    이 "Excel 다운로드 API" 구현 경험은 **금융권/공기업 백엔드 면접**에서 거의 확정적으로 나오는 주제예요. 본인 프로젝트에 하나 넣어두면 면접 질문의 80%에 자연스럽게 답할 수 있습니다.

### 🏗 Word 문서 (XWPFDocument)

```java
import org.apache.poi.xwpf.usermodel.*;

XWPFDocument doc = new XWPFDocument();

XWPFParagraph title = doc.createParagraph();
title.setAlignment(ParagraphAlignment.CENTER);
XWPFRun run = title.createRun();
run.setText("프로젝트 리포트");
run.setBold(true);
run.setFontSize(18);

XWPFTable table = doc.createTable(3, 2);
table.getRow(0).getCell(0).setText("날짜");
table.getRow(0).getCell(1).setText("진행 상황");

try (FileOutputStream fos = new FileOutputStream("report.docx")) {
    doc.write(fos);
}
doc.close();
```

!!! tip "💡 외워둘 것: Paragraph → Run 2단계"
    Apache POI의 Word는 **텍스트를 Paragraph → Run 2단계**로 추가합니다. 스타일(bold, color, size)은 Run에 걸립니다. 처음엔 이 2단계가 귀찮지만, 한 단락 안에서 글자마다 다른 스타일을 주려면 이 구조가 필수예요.

### 🤖 Claude Code로 200% 활용하기

!!! example "🤖 Claude Code 프롬프트 1: Excel 다운로드 API"
    ```
    내 Spring Boot 프로젝트에 "주문 내역 Excel 다운로드" API를 추가해줘.
    Order 엔티티를 OrderRepository로 조회해서 Apache POI로 .xlsx 파일을
    스트리밍 응답으로 내려주는 Controller + Service를 만들어줘.
    ```

!!! example "🤖 Claude Code 프롬프트 2: 스타일 유틸"
    ```
    POI에서 자주 쓰는 헤더 스타일(파란 배경 + 흰 글씨 + 가운데 정렬),
    통화 포맷 스타일, 날짜 포맷 스타일을 반환하는 CellStyleFactory 클래스를
    만들어줘.
    ```

!!! example "🤖 Claude Code 프롬프트 3: 대용량 처리"
    ```
    10만 행 이상의 Excel을 생성할 때 메모리 부족이 나고 있어. SXSSFWorkbook으로
    전환해서 스트리밍 방식으로 쓰는 방법을 알려주고, 기존 XSSFWorkbook 코드를
    변환해줘.
    ```

### 🚨 자주 발생하는 에러 Top 3

!!! danger "🚨 에러 1: `OutOfMemoryError`"
    **원인**: 10만 행 이상에서 `XSSFWorkbook`은 메모리에 전부 올림
    **해결**: `SXSSFWorkbook`(스트리밍 방식) 사용

!!! danger "🚨 에러 2: `NoClassDefFoundError: org/apache/xmlbeans/XmlObject`"
    **원인**: `poi-ooxml` 의존성 누락
    **해결**: `poi-ooxml`을 의존성에 추가

!!! danger "🚨 에러 3: 한글 폰트 깨짐"
    **해결**: `Font.setFontName("맑은 고딕")` 설정

### 📚 학습 체크리스트

- [ ] Gradle/Maven 의존성 추가 후 빌드 성공
- [ ] 기본 Excel 생성 및 Excel로 열어 확인
- [ ] 헤더 스타일 적용
- [ ] 기존 Excel 읽어서 콘솔 출력
- [ ] Spring Boot 다운로드 API 구현
- [ ] Word 문서 기본 생성

---

## 4-2-2. iText — PDF 생성 및 편집

**한 줄 소개**: Java 진영의 **최고 수준** PDF 라이브러리. 생성, 편집, 서명, 암호화까지 가능.

**왜 봐야 하는가**: 금융권/공공기관 프로젝트에서 PDF 전자문서는 필수입니다. iText는 전자서명, 암호화 같은 고급 기능까지 지원해서 기업용 프로젝트에 강해요.

**난이도**: ⭐⭐⭐

!!! warning "⚠️ 라이선스 주의"
    iText 7은 **AGPL**이에요. 오픈소스 프로젝트는 무료지만, 상용 제품에 쓰려면 상용 라이선스를 구매해야 합니다. 학습/포트폴리오용은 문제없어요. 상용 무료 대안은 **OpenPDF**(LGPL)이 있습니다.

### 📋 배울 수 있는 것

- PdfDocument / Document 계층 구조
- Paragraph, Table, Image, List 요소
- 폰트 설정(한글 폰트 포함)
- PDF 병합/분할
- 전자서명/암호화 기초

### 🚀 15분 퀵스타트

#### Step 1: 의존성

**Maven**:

```xml
<dependency>
    <groupId>com.itextpdf</groupId>
    <artifactId>itext7-core</artifactId>
    <version>8.0.2</version>
    <type>pom</type>
</dependency>
```

**Gradle**:

```groovy
implementation 'com.itextpdf:itext7-core:8.0.2'
```

#### Step 2: 첫 PDF 생성

```java
import com.itextpdf.kernel.pdf.PdfDocument;
import com.itextpdf.kernel.pdf.PdfWriter;
import com.itextpdf.layout.Document;
import com.itextpdf.layout.element.Paragraph;

public class PdfDemo {
    public static void main(String[] args) throws Exception {
        try (PdfWriter writer = new PdfWriter("hello.pdf");
             PdfDocument pdf = new PdfDocument(writer);
             Document document = new Document(pdf)) {

            document.add(new Paragraph("안녕하세요, iText!")
                .setBold()
                .setFontSize(18));
            document.add(new Paragraph("이것은 Java로 생성한 첫 PDF입니다."));
        }
        System.out.println("hello.pdf 생성 완료");
    }
}
```

#### Step 3: 표 추가

```java
import com.itextpdf.layout.element.Table;
import com.itextpdf.layout.element.Cell;

Table table = new Table(new float[]{1, 2, 1});
table.addHeaderCell(new Cell().add(new Paragraph("날짜").setBold()));
table.addHeaderCell(new Cell().add(new Paragraph("상품").setBold()));
table.addHeaderCell(new Cell().add(new Paragraph("수량").setBold()));

table.addCell("2026-04-01");
table.addCell("A상품");
table.addCell("10");

document.add(table);
```

#### Step 4: 한글 폰트 설정 ⭐중요⭐

```java
import com.itextpdf.io.font.PdfEncodings;
import com.itextpdf.kernel.font.PdfFont;
import com.itextpdf.kernel.font.PdfFontFactory;

PdfFont korean = PdfFontFactory.createFont(
    "C:/Windows/Fonts/malgun.ttf",
    PdfEncodings.IDENTITY_H,
    PdfFontFactory.EmbeddingStrategy.PREFER_EMBEDDED
);

document.setFont(korean);
document.add(new Paragraph("한글이 깨지지 않습니다!"));
```

!!! danger "🚨 한글 폰트 없이 한글을 쓰면 반드시 깨집니다"
    iText는 기본적으로 한글 폰트를 번들링하지 않아요. 운영체제의 `맑은 고딕`, `나눔고딕`, 또는 `NanumGothic.ttf`를 명시적으로 로드해야 합니다. 서버 배포 시에는 폰트 파일을 `resources/fonts/`에 넣고 절대 경로가 아닌 클래스패스로 로드하세요.

#### Step 5: 실행 확인

생성된 `hello.pdf`를 Acrobat Reader로 열어 확인.

### 💡 실전 패턴: Spring Boot에서 PDF 청구서 다운로드

```java
@RestController
@RequiredArgsConstructor
public class InvoiceController {

    private final InvoiceService service;

    @GetMapping("/api/invoices/{id}/download")
    public void download(@PathVariable Long id, HttpServletResponse response)
            throws Exception {
        Invoice invoice = service.findById(id);

        response.setContentType("application/pdf");
        response.setHeader(
            "Content-Disposition",
            "attachment; filename=invoice_" + id + ".pdf"
        );

        try (PdfWriter writer = new PdfWriter(response.getOutputStream());
             PdfDocument pdf = new PdfDocument(writer);
             Document doc = new Document(pdf)) {

            PdfFont font = PdfFontFactory.createFont(
                "fonts/NanumGothic.ttf",
                PdfEncodings.IDENTITY_H,
                PdfFontFactory.EmbeddingStrategy.PREFER_EMBEDDED
            );
            doc.setFont(font);

            doc.add(new Paragraph("청구서 #" + id).setBold().setFontSize(20));
            doc.add(new Paragraph("수신: " + invoice.getCustomer()));
            doc.add(new Paragraph("금액: " + invoice.getAmount() + "원"));
        }
    }
}
```

### 🤖 Claude Code로 200% 활용하기

!!! example "🤖 Claude Code 프롬프트 1: 템플릿 기반 생성"
    ```
    iText 8로 "회사 로고 + 주문 정보 + 상품 목록 표 + 합계" 구조의 주문 확인서
    PDF를 생성하는 유틸 클래스를 만들어줘. 한글 폰트는 classpath의
    fonts/NanumGothic.ttf를 쓸게. OrderDto를 인자로 받아.
    ```

!!! example "🤖 Claude Code 프롬프트 2: PDF 병합"
    ```
    여러 개의 PDF 파일을 하나로 합치는 PdfMerger 유틸을 iText로 작성해줘.
    페이지 번호도 전체 기준으로 다시 매겨줘.
    ```

!!! example "🤖 Claude Code 프롬프트 3: 워터마크"
    ```
    기존 PDF에 "DRAFT" 워터마크를 모든 페이지 대각선으로 추가하는
    함수를 만들어줘. 반투명 회색.
    ```

### 🚨 자주 발생하는 에러 Top 3

!!! danger "🚨 에러 1: 한글이 안 보이거나 깨짐"
    **해결**: `PdfFontFactory.createFont()`로 한글 TTF 로드 후 `doc.setFont()` 호출

!!! danger "🚨 에러 2: `Document is closed`"
    **원인**: `document.close()` 후 다시 추가하려 함
    **해결**: try-with-resources로 한 번에 끝내기

!!! danger "🚨 에러 3: 라이선스 경고"
    **원인**: iText 7/8은 상용 시 라이선스 필요
    **해결**: 상용이라면 라이선스 구매, 무료라면 **OpenPDF**로 전환

### 📚 학습 체크리스트

- [ ] 의존성 추가 및 빌드 성공
- [ ] 텍스트 + 표 포함 PDF 생성
- [ ] 한글 폰트 적용
- [ ] Spring Boot에서 PDF 다운로드 API 구현
- [ ] PDF 병합/분할 함수 작성
- [ ] 라이선스 이슈 이해

---

## 🎯 4-2 섹션을 마치며

Java 생태계에서는 **Apache POI + iText** 조합이 문서 자동화의 표준입니다. Spring Boot 프로젝트에 이 두 라이브러리를 활용한 기능을 하나만 추가해도 이력서에 쓸 수 있는 수준의 포트폴리오가 완성돼요.

다음은 브라우저/Node.js 환경을 위한 [4-3. JavaScript 문서 라이브러리](03-javascript.md)입니다.
