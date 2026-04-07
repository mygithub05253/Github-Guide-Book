# 4-1. Python 문서 라이브러리

> 이 섹션은 **이 가이드북을 만든 도구들**입니다. 한 번 익혀두면 평생 써먹을 수 있어요. 코드 예제는 전부 복사해서 바로 실행할 수 있도록 작성했습니다.

---

## 4-1-1. python-docx — Word 문서 생성

**한 줄 소개**: Python으로 `.docx` 파일을 만들고 편집할 수 있는 **사실상 표준** 라이브러리.

**왜 봐야 하는가**: 주간 보고서, 계약서, 이력서, 자동화된 서식 문서의 95%가 python-docx로 해결됩니다. 이 가이드북의 Word 버전도 여기서 나왔어요.

**난이도**: ⭐⭐

### 📋 이 레포에서 배울 수 있는 것

- Heading, Paragraph, Run의 계층 구조
- 표(Table) 생성 및 스타일 적용
- 이미지 삽입
- 기존 Word 문서 읽고 수정하기
- 스타일 템플릿 활용

### 🚀 15분 퀵스타트

#### Step 1: 설치

```bash
pip install python-docx
```

!!! info "예상 출력"
    ```
    Successfully installed python-docx-1.1.0 lxml-5.1.0
    ```

!!! warning "⚠️ 주의"
    패키지 이름은 `python-docx`이지만, `import`는 `from docx import ...`입니다. `import python_docx`로 썼다가 `ModuleNotFoundError`가 나는 실수가 정말 자주 일어나요.

#### Step 2: 첫 Word 문서 만들기

```python
from docx import Document

doc = Document()
doc.add_heading('내 첫 자동화 보고서', level=0)
doc.add_paragraph('이 문서는 Python으로 생성되었습니다.')
doc.save('hello.docx')
```

#### Step 3: 실행 및 결과 확인

```bash
python first_docx.py
```

생성된 `hello.docx`를 Word에서 열어보세요. 제목과 본문이 들어간 실제 Word 문서가 보입니다.

#### Step 4: 표 추가

```python
from docx import Document

doc = Document()
doc.add_heading('2026 Q1 매출', level=1)

table = doc.add_table(rows=3, cols=3)
table.style = 'Light Grid Accent 1'

headers = ['월', '매출', '증감']
for i, h in enumerate(headers):
    table.rows[0].cells[i].text = h

data = [('1월', '1,200만', '+5%'), ('2월', '1,350만', '+12%')]
for r, row_data in enumerate(data, start=1):
    for c, value in enumerate(row_data):
        table.rows[r].cells[c].text = value

doc.save('sales_report.docx')
```

#### Step 5: 이미지 삽입

```python
from docx import Document
from docx.shared import Inches

doc = Document()
doc.add_heading('차트 포함 보고서', level=1)
doc.add_picture('chart.png', width=Inches(5))
doc.save('with_image.docx')
```

!!! info "예상 출력"
    이미지가 본문에 포함된 `with_image.docx` 파일 생성. Word에서 열면 5인치 너비의 차트가 중앙에 보입니다.

### 🏗 핵심 API 치트시트

| 메서드 | 용도 |
|---|---|
| `Document()` | 새 문서 생성 |
| `Document('existing.docx')` | 기존 문서 열기 |
| `doc.add_heading(text, level)` | 제목 (level 0=Title, 1=H1, ...) |
| `doc.add_paragraph(text, style)` | 본문 단락 |
| `doc.add_table(rows, cols)` | 표 |
| `doc.add_picture(path, width)` | 이미지 |
| `doc.add_page_break()` | 페이지 나누기 |
| `doc.save(path)` | 저장 |

### 💡 실전 패턴: 반복 보고서 자동 생성

```python
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

def generate_weekly_report(week_num, data):
    doc = Document()

    # 제목
    title = doc.add_heading(f'{week_num}주차 주간 보고서', level=0)
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER

    # 요약 문단
    summary = doc.add_paragraph()
    summary.add_run('핵심 지표: ').bold = True
    summary.add_run(f"매출 {data['revenue']}, 신규 사용자 {data['new_users']}")

    # 상세 표
    doc.add_heading('카테고리별 매출', level=1)
    table = doc.add_table(rows=1 + len(data['categories']), cols=2)
    table.style = 'Light List Accent 1'
    table.rows[0].cells[0].text = '카테고리'
    table.rows[0].cells[1].text = '매출'
    for i, (cat, rev) in enumerate(data['categories'].items(), start=1):
        table.rows[i].cells[0].text = cat
        table.rows[i].cells[1].text = f'{rev:,}원'

    doc.save(f'report_week{week_num}.docx')

# 실행
generate_weekly_report(15, {
    'revenue': '2,400만원',
    'new_users': 132,
    'categories': {'전자': 12000000, '의류': 8000000, '식품': 4000000},
})
```

### 🤖 Claude Code로 200% 활용하기

!!! example "🤖 Claude Code 프롬프트 1: 이력서 자동 생성"
    ```
    내 정보(이름, 학교, 경력, 스킬, 프로젝트)를 dict로 줄게. 이걸 받아서
    python-docx로 한국어 IT 직무 이력서 템플릿(2페이지)을 만드는 함수를
    작성해줘. 스타일은 깔끔한 미니멀 디자인.
    ```

!!! example "🤖 Claude Code 프롬프트 2: 템플릿 필러"
    ```
    template.docx 파일의 {{이름}}, {{날짜}}, {{금액}} 같은 플레이스홀더를
    dict로 치환해서 새 파일로 저장하는 `render_template(template, context, output)`
    함수를 만들어줘. 서식은 그대로 유지해야 해.
    ```

!!! example "🤖 Claude Code 프롬프트 3: 표 스타일 적용"
    ```
    python-docx에서 표 헤더 행을 파란 배경+흰 글씨로 만드는 방법을 알려줘.
    XML 직접 조작이 필요하다면 헬퍼 함수 형태로 작성해줘.
    ```

### 🚨 자주 발생하는 에러 Top 3

!!! danger "🚨 에러 1: `ModuleNotFoundError: No module named 'docx'`"
    **원인**: `pip install docx`로 잘못 설치 (docx는 다른 패키지)
    **해결**:
    ```bash
    pip uninstall docx
    pip install python-docx
    ```

!!! danger "🚨 에러 2: 한글 폰트 깨짐"
    **원인**: 기본 폰트가 한글을 지원하지 않음
    **해결**:
    ```python
    from docx.oxml.ns import qn
    style = doc.styles['Normal']
    style.font.name = '맑은 고딕'
    style.element.rPr.rFonts.set(qn('w:eastAsia'), '맑은 고딕')
    ```

!!! danger "🚨 에러 3: `PackageNotFoundError: Package not found at ...`"
    **원인**: 파일 경로가 잘못됐거나, 파일이 이미 Word에서 열려있음
    **해결**: Word에서 파일 닫기, 절대 경로 사용

### 📚 학습 체크리스트

- [ ] python-docx 설치 성공
- [ ] Heading + Paragraph + Table + Image가 들어간 문서 생성
- [ ] 기존 Word 파일 읽어서 모든 문단 출력
- [ ] 반복 데이터로 문서 10개 자동 생성
- [ ] 한글 폰트 설정 적용

---

## 4-1-2. openpyxl — Excel 파일 처리

**한 줄 소개**: Python으로 `.xlsx` 파일을 **읽고, 쓰고, 스타일까지 입힐 수 있는** 라이브러리.

**왜 봐야 하는가**: 직장에서 Excel 없이 일하는 건 불가능해요. openpyxl은 수식, 차트, 피벗, 조건부 서식까지 지원합니다.

**난이도**: ⭐⭐

### 📋 이 레포에서 배울 수 있는 것

- Workbook / Worksheet / Cell 구조
- 데이터 쓰기/읽기 (단일 셀 vs 범위)
- Font, PatternFill, Alignment, Border 스타일
- 수식 입력 (`=SUM(A1:A10)`)
- 차트 생성

### 🚀 15분 퀵스타트

#### Step 1: 설치

```bash
pip install openpyxl
```

#### Step 2: 첫 Excel 파일

```python
from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws.title = "Sales"

ws.append(['날짜', '상품', '수량', '가격', '합계'])
ws.append(['2026-04-01', 'A상품', 10, 50000, None])
ws.append(['2026-04-02', 'B상품', 15, 30000, None])

# E열에 수식 추가
ws['E2'] = '=C2*D2'
ws['E3'] = '=C3*D3'

wb.save('sales.xlsx')
```

#### Step 3: 실행 → Excel로 열어보기

결과 파일을 Excel에서 열면 E2, E3 셀에 **자동 계산된 값**이 들어가 있어요.

#### Step 4: 헤더 스타일링

```python
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment

wb = Workbook()
ws = wb.active

ws.append(['날짜', '상품', '수량', '가격', '합계'])

# 헤더 행만 꾸미기
for cell in ws[1]:
    cell.font = Font(bold=True, color="FFFFFF", size=12)
    cell.fill = PatternFill("solid", fgColor="4472C4")
    cell.alignment = Alignment(horizontal="center", vertical="center")

ws.column_dimensions['A'].width = 12
ws.column_dimensions['B'].width = 15
ws.row_dimensions[1].height = 25

wb.save('styled.xlsx')
```

#### Step 5: 기존 파일 읽기

```python
from openpyxl import load_workbook

wb = load_workbook('sales.xlsx')
ws = wb.active

for row in ws.iter_rows(min_row=2, values_only=True):
    print(row)
```

!!! info "예상 출력"
    ```
    ('2026-04-01', 'A상품', 10, 50000, 500000)
    ('2026-04-02', 'B상품', 15, 30000, 450000)
    ```

### 💡 실전 패턴: 일일 매출 집계 스크립트

```python
from openpyxl import load_workbook
from collections import defaultdict

wb = load_workbook('sales.xlsx')
ws = wb.active

# 상품별 합계
totals = defaultdict(int)
for row in ws.iter_rows(min_row=2, values_only=True):
    date, product, qty, price, total = row
    if total:
        totals[product] += total

print("상품별 총 매출:")
for product, total in sorted(totals.items(), key=lambda x: -x[1]):
    print(f"  {product}: {total:,}원")
```

### 🤖 Claude Code로 200% 활용하기

!!! example "🤖 Claude Code 프롬프트 1: 다중 시트 생성"
    ```
    openpyxl로 "월별" 시트 12개가 있는 워크북을 만들고, 각 시트마다 "일자/매출/비용/이익"
    4열 헤더와 31일치 빈 행을 준비하는 스크립트를 작성해줘. 헤더는 파란 배경에 흰 글씨.
    ```

!!! example "🤖 Claude Code 프롬프트 2: 차트 추가"
    ```
    sales.xlsx를 읽어서 상품별 매출 합계를 계산한 뒤, 같은 파일의 새 시트에
    막대 차트(BarChart)를 추가하는 스크립트를 만들어줘.
    ```

!!! example "🤖 Claude Code 프롬프트 3: CSV → Excel 변환"
    ```
    폴더 안의 모든 .csv를 읽어서, 각각을 시트로 가진 하나의 .xlsx로 합쳐줘.
    시트 이름은 파일명(확장자 제외), 헤더 행은 자동으로 bold.
    ```

### 🚨 자주 발생하는 에러 Top 3

!!! danger "🚨 에러 1: `InvalidFileException`"
    **원인**: `.xls`(구버전)를 열려고 함. openpyxl은 `.xlsx`만 지원
    **해결**: `xlrd` 또는 `pandas.read_excel`로 `.xls` 처리

!!! danger "🚨 에러 2: 수식이 계산되지 않음 (값이 None)"
    **원인**: `load_workbook(..., data_only=True)`를 안 씀
    **해결**:
    ```python
    wb = load_workbook('sales.xlsx', data_only=True)
    ```
    단, 이는 Excel이 한 번이라도 파일을 저장한 후에만 동작

!!! danger "🚨 에러 3: `PermissionError` (저장 실패)"
    **원인**: 파일이 Excel에서 열려있음
    **해결**: Excel 종료 후 재시도

### 📚 학습 체크리스트

- [ ] 기본 데이터 쓰기/읽기 성공
- [ ] 헤더 스타일(Font/Fill/Alignment) 적용
- [ ] 수식 입력 및 `data_only=True`로 값 읽기
- [ ] 다중 시트 생성
- [ ] 차트 1개 추가

---

## 4-1-3. python-pptx — PowerPoint 생성

**한 줄 소개**: `.pptx` 파일을 Python으로 생성/편집하는 라이브러리. 발표자료 자동화에 최적.

**왜 봐야 하는가**: 매주 같은 형식의 발표자료를 만드는 건 고통입니다. 템플릿 + 데이터 → 슬라이드 자동 생성으로 해결하세요.

**난이도**: ⭐⭐⭐

### 📋 이 레포에서 배울 수 있는 것

- Slide Layout 개념과 활용
- 제목/텍스트 placeholder 채우기
- 이미지, 차트, 표 삽입
- 템플릿 기반 슬라이드 양산

### 🚀 15분 퀵스타트

#### Step 1: 설치

```bash
pip install python-pptx
```

#### Step 2: 제목 슬라이드

```python
from pptx import Presentation

prs = Presentation()
slide = prs.slides.add_slide(prs.slide_layouts[0])   # 0 = Title Slide
slide.shapes.title.text = "2026 Q1 프로젝트 리뷰"
slide.placeholders[1].text = "발표자: 홍길동 | 2026-04-07"
prs.save('first_deck.pptx')
```

#### Step 3: 내용 슬라이드 (bullet list)

```python
slide = prs.slides.add_slide(prs.slide_layouts[1])   # 1 = Title and Content
slide.shapes.title.text = "이번 분기 성과"

body = slide.placeholders[1].text_frame
body.text = "매출 전년 대비 25% 성장"
body.add_paragraph().text = "신규 사용자 12만 명"
body.add_paragraph().text = "앱 평점 4.8 유지"
prs.save('first_deck.pptx')
```

#### Step 4: 차트 슬라이드

```python
from pptx import Presentation
from pptx.util import Inches
from pptx.chart.data import CategoryChartData
from pptx.enum.chart import XL_CHART_TYPE

prs = Presentation()
slide = prs.slides.add_slide(prs.slide_layouts[5])   # 5 = Blank

chart_data = CategoryChartData()
chart_data.categories = ['1월', '2월', '3월']
chart_data.add_series('매출(만원)', (1200, 1350, 1580))

slide.shapes.add_chart(
    XL_CHART_TYPE.COLUMN_CLUSTERED,
    Inches(1), Inches(1.5), Inches(8), Inches(5),
    chart_data,
)
prs.save('with_chart.pptx')
```

#### Step 5: 실행 확인

PowerPoint(또는 LibreOffice Impress, Keynote)에서 `with_chart.pptx`를 열어 차트 슬라이드 확인.

!!! tip "💡 꿀팁: 슬라이드 레이아웃 번호 기억법"
    | 번호 | 이름 | 용도 |
    |---|---|---|
    | 0 | Title Slide | 표지 |
    | 1 | Title and Content | 일반 내용 |
    | 5 | Blank | 자유 배치(차트/이미지) |

### 🤖 Claude Code로 200% 활용하기

!!! example "🤖 Claude Code 프롬프트 1: 데이터 → 발표 자료"
    ```
    내가 dict 리스트로 "월/매출/비용/이익"을 줄게. 이걸 받아서
    python-pptx로 표지 + 월별 차트 + 요약 총 3슬라이드를 자동 생성하는
    함수를 만들어줘.
    ```

!!! example "🤖 Claude Code 프롬프트 2: 템플릿 활용"
    ```
    회사 template.pptx를 열어서 첫 번째 슬라이드(제목 슬라이드)의 제목과
    발표자 텍스트만 바꾸고 다른 이름으로 저장하는 스크립트를 만들어줘.
    나머지 슬라이드는 그대로 유지.
    ```

!!! example "🤖 Claude Code 프롬프트 3: 이미지 양산"
    ```
    폴더 안의 PNG 파일들을 각각 1장씩 가지는 슬라이드쇼 pptx를 만들어줘.
    각 슬라이드 제목은 파일명, 이미지는 중앙 정렬.
    ```

### 🚨 자주 발생하는 에러 Top 3

!!! danger "🚨 에러 1: `AttributeError: 'NoneType' has no attribute 'text'`"
    **원인**: 해당 레이아웃에 placeholder가 없는데 `placeholders[1]` 접근
    **해결**: `for ph in slide.placeholders: print(ph.placeholder_format.idx, ph.name)`로 확인

!!! danger "🚨 에러 2: 한글 폰트 깨짐"
    **해결**: `text_frame.paragraphs[0].runs[0].font.name = '맑은 고딕'`

!!! danger "🚨 에러 3: 이미지 크기가 원본 크기로 들어감"
    **해결**: `add_picture(path, left, top, width=Inches(8))`로 width 지정

### 📚 학습 체크리스트

- [ ] 제목 슬라이드 + 내용 슬라이드 생성
- [ ] 차트 슬라이드 추가
- [ ] 이미지 포함 슬라이드
- [ ] 기존 템플릿을 열어 내용만 수정
- [ ] 데이터 리스트로 슬라이드 5장 자동 생성

---

## 4-1-4. PyMuPDF (fitz) — PDF 처리

**한 줄 소개**: PDF 읽기/쓰기/편집/텍스트 추출/이미지 추출을 **한 라이브러리**로 해결하는 강력한 도구.

**왜 봐야 하는가**: PDF에서 데이터를 뽑아야 할 일이 생기면 (대학 공지사항, 논문, 보고서 등) PyMuPDF 하나면 충분합니다. 속도도 PyPDF2보다 10배 빨라요.

**난이도**: ⭐⭐⭐

### 📋 이 레포에서 배울 수 있는 것

- PDF 페이지별 텍스트 추출
- 이미지 추출
- 새 PDF 생성 및 그리기
- PDF 병합/분할
- 하이라이트/주석 추가

### 🚀 15분 퀵스타트

#### Step 1: 설치

```bash
pip install PyMuPDF
```

!!! warning "⚠️ 주의"
    패키지명은 `PyMuPDF`이지만 `import`는 `import fitz`예요. 역사적 이유입니다.

#### Step 2: 텍스트 추출

```python
import fitz

doc = fitz.open('sample.pdf')
print(f"총 페이지: {len(doc)}")

for i, page in enumerate(doc):
    text = page.get_text()
    print(f"--- 페이지 {i+1} ---")
    print(text[:200])   # 앞 200자만

doc.close()
```

#### Step 3: 이미지 추출

```python
import fitz

doc = fitz.open('sample.pdf')

for page_num, page in enumerate(doc):
    for img_idx, img in enumerate(page.get_images()):
        xref = img[0]
        pix = fitz.Pixmap(doc, xref)
        if pix.n - pix.alpha < 4:   # RGB 또는 Grayscale
            pix.save(f'p{page_num}_img{img_idx}.png')
        else:   # CMYK → RGB 변환
            pix = fitz.Pixmap(fitz.csRGB, pix)
            pix.save(f'p{page_num}_img{img_idx}.png')

doc.close()
```

#### Step 4: 새 PDF 생성

```python
import fitz

doc = fitz.open()
page = doc.new_page()

page.insert_text((50, 50), "안녕하세요, PyMuPDF!", fontsize=16)
page.draw_rect((50, 100, 300, 200), color=(0, 0, 1), width=2)

doc.save('generated.pdf')
doc.close()
```

#### Step 5: 페이지 분할

```python
import fitz

doc = fitz.open('big.pdf')

# 1-3 페이지만 추출
new_doc = fitz.open()
new_doc.insert_pdf(doc, from_page=0, to_page=2)
new_doc.save('pages_1_to_3.pdf')

doc.close()
new_doc.close()
```

### 💡 실전 패턴: 대학 공지 PDF에서 키워드 검색

```python
import fitz

def search_pdf(pdf_path, keyword):
    doc = fitz.open(pdf_path)
    results = []
    for page_num, page in enumerate(doc):
        text = page.get_text()
        if keyword in text:
            # 키워드가 포함된 문장 추출
            for line in text.split('\n'):
                if keyword in line:
                    results.append((page_num + 1, line.strip()))
    doc.close()
    return results

for page, line in search_pdf('공지.pdf', '장학금'):
    print(f"[p.{page}] {line}")
```

### 🤖 Claude Code로 200% 활용하기

!!! example "🤖 Claude Code 프롬프트 1: PDF → Markdown"
    ```
    PyMuPDF로 input.pdf를 페이지별로 읽어서 Markdown 파일로 저장하는
    스크립트를 만들어줘. 제목은 `#`, 단락은 빈 줄로 구분, 페이지 번호는 `---`로.
    ```

!!! example "🤖 Claude Code 프롬프트 2: 표 데이터 추출"
    ```
    PDF의 표 데이터를 추출해서 CSV로 변환하는 함수를 만들어줘.
    PyMuPDF의 find_tables() 메서드를 사용해.
    ```

!!! example "🤖 Claude Code 프롬프트 3: 워터마크 추가"
    ```
    모든 페이지 중앙에 반투명 "CONFIDENTIAL" 텍스트 워터마크를 45도 기울여서
    추가하는 스크립트를 만들어줘.
    ```

### 🚨 자주 발생하는 에러 Top 3

!!! danger "🚨 에러 1: `import fitz` 실패"
    **원인**: `fitz`라는 이름의 다른 패키지가 설치됨
    **해결**:
    ```bash
    pip uninstall fitz
    pip install PyMuPDF
    ```

!!! danger "🚨 에러 2: 한글 텍스트가 깨짐"
    **원인**: PDF가 스캔본(이미지)이거나 임베딩 폰트 문제
    **해결**: OCR 필요 → `pytesseract` 또는 `PaddleOCR` 추가 사용

!!! danger "🚨 에러 3: `doc.close()` 누락 → 파일 잠김"
    **해결**: `with fitz.open(path) as doc:` 컨텍스트 매니저 사용

### 📚 학습 체크리스트

- [ ] PDF 전체 텍스트 추출
- [ ] 이미지 추출 성공
- [ ] 새 PDF 생성 (텍스트 + 도형)
- [ ] 페이지 분할/병합
- [ ] 키워드 검색 함수 작성

---

## 🎯 4-1 섹션을 마치며

여기까지 왔다면 당신은 **Word, Excel, PowerPoint, PDF를 자유자재로 다루는 Python 개발자**가 되었어요. 이미 이 지점에서 대부분의 업무 자동화가 가능합니다.

다음은 Java 생태계가 궁금한 분들을 위한 [4-2. Java 문서 라이브러리](02-java.md), 브라우저/Node.js가 필요한 분들을 위한 [4-3. JavaScript 문서 라이브러리](03-javascript.md)를 준비했어요. 본인 스택에 맞는 섹션으로 넘어가세요.

그리고 가장 재미있는 [4-4. 문서 자동화 파이프라인](04-pipeline.md)에서 **이 가이드북 자체를 직접 빌드해보는** 미니 튜토리얼이 기다리고 있습니다.
