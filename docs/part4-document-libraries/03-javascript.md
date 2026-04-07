# 4-3. JavaScript 문서 라이브러리

> "버튼을 누르면 Excel이 바로 다운로드되는" 브라우저 기능을 만들어본 적 있나요? 그게 SheetJS로 가능해요. JavaScript 생태계의 문서 라이브러리는 **클라이언트 사이드**에서 문서를 생성할 수 있다는 엄청난 장점이 있습니다.

---

## 4-3-1. SheetJS (xlsx) — Excel 처리

**한 줄 소개**: **브라우저와 Node.js 모두**에서 동작하는 JavaScript 최강 Excel 라이브러리.

**왜 봐야 하는가**: React/Next.js 앱에서 "Excel 다운로드" 버튼을 만들어야 할 때 이것 하나면 됩니다. 서버 왕복 없이 **브라우저에서 바로** 파일을 만들어 다운로드할 수 있어요.

**난이도**: ⭐⭐

### 📋 배울 수 있는 것

- `.xlsx` 파일 읽기/쓰기
- JSON ↔ Worksheet 변환
- 브라우저 다운로드 트리거
- Node.js에서 파일 생성
- CSV, JSON, HTML 테이블 간 변환

### 🚀 15분 퀵스타트 (Node.js)

#### Step 1: 설치

```bash
npm install xlsx
```

#### Step 2: Excel 파일 생성 (Node.js)

```javascript
const XLSX = require('xlsx');

const data = [
  { 날짜: '2026-04-01', 상품: 'A상품', 수량: 10, 가격: 50000 },
  { 날짜: '2026-04-02', 상품: 'B상품', 수량: 15, 가격: 30000 },
];

const worksheet = XLSX.utils.json_to_sheet(data);
const workbook = XLSX.utils.book_new();
XLSX.utils.book_append_sheet(workbook, worksheet, 'Sales');
XLSX.writeFile(workbook, 'sales.xlsx');

console.log('sales.xlsx 생성 완료');
```

!!! info "예상 출력"
    ```
    sales.xlsx 생성 완료
    ```

#### Step 3: Excel 파일 읽기

```javascript
const XLSX = require('xlsx');

const workbook = XLSX.readFile('sales.xlsx');
const sheet = workbook.Sheets[workbook.SheetNames[0]];
const data = XLSX.utils.sheet_to_json(sheet);

console.log(data);
```

### 🌐 브라우저(React)에서 Excel 다운로드

```typescript
import * as XLSX from 'xlsx';

function DownloadButton({ data }: { data: Sale[] }) {
  const handleDownload = () => {
    const worksheet = XLSX.utils.json_to_sheet(data);
    const workbook = XLSX.utils.book_new();
    XLSX.utils.book_append_sheet(workbook, worksheet, 'Sales');
    XLSX.writeFile(workbook, `sales_${Date.now()}.xlsx`);
  };

  return <button onClick={handleDownload}>Excel 다운로드</button>;
}
```

!!! tip "💡 꿀팁: 서버 부하 0"
    이 방식은 **브라우저에서 직접 파일을 생성**해서 서버로 왕복이 필요 없어요. 대용량 데이터(수만 행)도 사용자 컴퓨터 자원으로 처리되니 서버 비용이 절약됩니다.

### 🌐 브라우저에서 Excel 파일 업로드 → 파싱

```typescript
function UploadExcel() {
  const handleFile = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) return;

    const reader = new FileReader();
    reader.onload = (event) => {
      const data = new Uint8Array(event.target!.result as ArrayBuffer);
      const workbook = XLSX.read(data, { type: 'array' });
      const sheet = workbook.Sheets[workbook.SheetNames[0]];
      const json = XLSX.utils.sheet_to_json(sheet);
      console.log('파싱 결과:', json);
    };
    reader.readAsArrayBuffer(file);
  };

  return <input type="file" accept=".xlsx,.xls" onChange={handleFile} />;
}
```

### 🤖 Claude Code로 200% 활용하기

!!! example "🤖 Claude Code 프롬프트 1: 템플릿 컴포넌트"
    ```
    React 컴포넌트 <ExcelExportButton data={...} columns={...} filename="..." />를
    만들어줘. columns는 {key, label, width} 배열이고, SheetJS로 스타일 적용된
    Excel을 다운로드하게 해줘. TypeScript strict 모드.
    ```

!!! example "🤖 Claude Code 프롬프트 2: CSV 업로드 파서"
    ```
    사용자가 CSV를 드래그앤드롭하면 파싱해서 미리보기 테이블을 보여주고,
    유효성 검사(필수 컬럼 존재 여부)를 하는 Next.js 페이지를 만들어줘.
    xlsx 라이브러리를 쓸게.
    ```

!!! example "🤖 Claude Code 프롬프트 3: 다중 시트 export"
    ```
    데이터를 카테고리별로 그룹화해서 각 그룹을 별도 시트로 가지는
    Excel 파일을 만드는 함수를 TypeScript로 작성해줘.
    ```

### 🚨 자주 발생하는 에러 Top 3

!!! danger "🚨 에러 1: `XLSX is not defined` (브라우저)"
    **원인**: import 누락 또는 CDN 로드 실패
    **해결**: `import * as XLSX from 'xlsx'`

!!! danger "🚨 에러 2: 날짜가 숫자(45000 같은 값)로 표시됨"
    **원인**: Excel은 날짜를 1900년 기준 일수로 저장
    **해결**: `cellDates: true` 옵션 사용
    ```javascript
    XLSX.read(data, { type: 'array', cellDates: true });
    ```

!!! danger "🚨 에러 3: 한글 파일명이 깨짐"
    **해결**: 파일명에 영문 + 타임스탬프 사용 권장 (`sales_20260407.xlsx`)

### 📚 학습 체크리스트

- [ ] Node.js에서 Excel 생성
- [ ] 기존 Excel 읽어 JSON 변환
- [ ] React에서 다운로드 버튼 구현
- [ ] 파일 업로드 후 파싱
- [ ] 다중 시트 워크북 생성

---

## 4-3-2. PDFKit — Node.js PDF 생성

**한 줄 소개**: Node.js에서 **프로그래밍 방식으로** PDF를 그리는 라이브러리. 스트리밍 방식이라 대용량에 강합니다.

**왜 봐야 하는가**: Express 백엔드에서 PDF 청구서/증명서/리포트를 생성해야 할 때 표준입니다.

**난이도**: ⭐⭐⭐

### 📋 배울 수 있는 것

- 스트리밍 방식 PDF 생성
- 텍스트, 이미지, 도형 그리기
- 폰트 임베딩 (한글)
- 페이지 추가 및 레이아웃
- Express 응답으로 스트리밍

### 🚀 15분 퀵스타트

#### Step 1: 설치

```bash
npm install pdfkit
```

#### Step 2: 첫 PDF

```javascript
const PDFDocument = require('pdfkit');
const fs = require('fs');

const doc = new PDFDocument();
doc.pipe(fs.createWriteStream('output.pdf'));

doc.fontSize(25).text('프로젝트 리포트', { align: 'center' });
doc.moveDown();
doc.fontSize(12).text('작성일: 2026-04-07');
doc.moveDown();
doc.text('이것은 PDFKit으로 생성한 첫 PDF입니다.');

doc.end();
console.log('output.pdf 생성 완료');
```

#### Step 3: 한글 폰트 ⭐중요⭐

```javascript
const PDFDocument = require('pdfkit');
const fs = require('fs');

const doc = new PDFDocument();
doc.pipe(fs.createWriteStream('korean.pdf'));

// 한글 폰트 등록
doc.registerFont('Nanum', 'fonts/NanumGothic.ttf');
doc.font('Nanum');

doc.fontSize(20).text('한글 PDF가 잘 나옵니다!');
doc.end();
```

!!! warning "⚠️ 한글 폰트 필수"
    PDFKit 기본 폰트(Helvetica)는 한글을 지원하지 않아 네모로 표시됩니다. 반드시 `.ttf` 파일을 등록하세요. 나눔고딕은 무료 라이선스라 상용 프로젝트에도 써도 됩니다.

#### Step 4: 표 직접 그리기 (PDFKit은 표 API가 없음)

```javascript
function drawTable(doc, headers, rows, x, y, colWidth, rowHeight) {
  // 헤더
  headers.forEach((h, i) => {
    doc.rect(x + i * colWidth, y, colWidth, rowHeight).stroke();
    doc.text(h, x + i * colWidth + 5, y + 5);
  });

  // 데이터
  rows.forEach((row, r) => {
    row.forEach((cell, c) => {
      const yPos = y + (r + 1) * rowHeight;
      doc.rect(x + c * colWidth, yPos, colWidth, rowHeight).stroke();
      doc.text(String(cell), x + c * colWidth + 5, yPos + 5);
    });
  });
}

const doc = new PDFDocument();
doc.pipe(fs.createWriteStream('table.pdf'));

drawTable(
  doc,
  ['날짜', '상품', '수량'],
  [['04-01', 'A', 10], ['04-02', 'B', 15]],
  50, 100, 100, 25
);

doc.end();
```

#### Step 5: Express 응답 스트리밍

```javascript
const express = require('express');
const PDFDocument = require('pdfkit');

const app = express();

app.get('/invoice/:id', (req, res) => {
  const doc = new PDFDocument();

  res.setHeader('Content-Type', 'application/pdf');
  res.setHeader('Content-Disposition', `attachment; filename=invoice_${req.params.id}.pdf`);

  doc.pipe(res);

  doc.fontSize(20).text(`청구서 #${req.params.id}`);
  doc.fontSize(12).text('금액: 50,000원');

  doc.end();
});

app.listen(3000);
```

### 🤖 Claude Code로 200% 활용하기

!!! example "🤖 Claude Code 프롬프트 1: 청구서 템플릿"
    ```
    PDFKit으로 "회사 로고 + 청구 정보 + 항목 테이블 + 합계 + 서명란" 구조의
    청구서 PDF 생성 함수를 만들어줘. invoice 객체를 받아서 Buffer를 반환해.
    한글 폰트는 fonts/NanumGothic.ttf 사용.
    ```

!!! example "🤖 Claude Code 프롬프트 2: 증명서 대량 생성"
    ```
    수강생 배열을 받아서 각자에게 수료증 PDF를 생성하는 스크립트를 만들어줘.
    파일명은 수강생 이름.pdf, 템플릿 배경 이미지 위에 이름과 날짜를 덮어써.
    ```

!!! example "🤖 Claude Code 프롬프트 3: 페이지 번호"
    ```
    PDFKit 문서의 모든 페이지 하단에 "페이지 N / 총 M" 형식으로 번호를
    자동으로 찍는 함수를 만들어줘. pageAdded 이벤트를 활용해.
    ```

### 🚨 자주 발생하는 에러 Top 3

!!! danger "🚨 에러 1: 한글이 네모로 표시"
    **해결**: 한글 TTF 등록 후 `doc.font('한글폰트')` 호출

!!! danger "🚨 에러 2: `doc.end()` 전에 파일이 빔"
    **원인**: 스트림이 닫히지 않음
    **해결**: 반드시 마지막에 `doc.end()`

!!! danger "🚨 에러 3: Express 응답에서 PDF가 깨짐"
    **원인**: `Content-Type` 헤더 누락 또는 다른 미들웨어가 응답 간섭
    **해결**: `res.setHeader('Content-Type', 'application/pdf')` 먼저 호출

### 📚 학습 체크리스트

- [ ] Node.js에서 기본 PDF 생성
- [ ] 한글 폰트 등록 및 적용
- [ ] 표 헬퍼 함수 작성
- [ ] Express로 PDF 다운로드 API 구현
- [ ] 페이지 번호 자동 삽입

---

## 4-3-3. docx — Word 문서 생성 (JS)

**한 줄 소개**: JavaScript/TypeScript로 `.docx` 파일을 만드는 **선언형** 라이브러리.

**왜 봐야 하는가**: Node.js 백엔드나 브라우저에서 Word 문서를 생성해야 할 때 씁니다. `python-docx`의 JS 버전이라고 생각하면 돼요.

**난이도**: ⭐⭐⭐

### 📋 배울 수 있는 것

- 선언형 Document 구조
- Paragraph, Run, Table 요소
- 스타일 및 포맷팅
- Node.js에서 파일 저장, 브라우저에서 Blob 다운로드

### 🚀 15분 퀵스타트

#### Step 1: 설치

```bash
npm install docx
```

#### Step 2: 기본 문서 생성

```typescript
import {
  Document, Packer, Paragraph, TextRun, HeadingLevel,
} from 'docx';
import * as fs from 'fs';

const doc = new Document({
  sections: [{
    children: [
      new Paragraph({
        text: '프로젝트 리포트',
        heading: HeadingLevel.HEADING_1,
      }),
      new Paragraph({
        children: [
          new TextRun('작성일: '),
          new TextRun({ text: '2026-04-07', bold: true }),
        ],
      }),
      new Paragraph('이 문서는 TypeScript로 생성되었습니다.'),
    ],
  }],
});

Packer.toBuffer(doc).then((buffer) => {
  fs.writeFileSync('report.docx', buffer);
  console.log('report.docx 생성 완료');
});
```

#### Step 3: 표 추가

```typescript
import {
  Document, Packer, Paragraph, Table, TableRow, TableCell, WidthType,
} from 'docx';

const cell = (text: string) => new TableCell({
  children: [new Paragraph(text)],
  width: { size: 3000, type: WidthType.DXA },
});

const doc = new Document({
  sections: [{
    children: [
      new Paragraph({ text: '매출 현황', heading: 'Heading1' as any }),
      new Table({
        rows: [
          new TableRow({ children: [cell('날짜'), cell('상품'), cell('매출')] }),
          new TableRow({ children: [cell('04-01'), cell('A'), cell('50,000')] }),
          new TableRow({ children: [cell('04-02'), cell('B'), cell('45,000')] }),
        ],
      }),
    ],
  }],
});

Packer.toBuffer(doc).then((buf) => fs.writeFileSync('sales.docx', buf));
```

#### Step 4: 브라우저 다운로드

```typescript
import { Document, Packer, Paragraph } from 'docx';
import { saveAs } from 'file-saver';

async function downloadReport() {
  const doc = new Document({
    sections: [{ children: [new Paragraph('Hello World')] }],
  });

  const blob = await Packer.toBlob(doc);
  saveAs(blob, 'report.docx');
}
```

!!! tip "💡 꿀팁: python-docx vs docx(JS) 비교"
    | 항목 | python-docx | docx (JS) |
    |---|---|---|
    | 스타일 | 명령형 (`.add_paragraph()`) | 선언형 (React 비슷) |
    | 학습 곡선 | 쉬움 | 중간 |
    | 브라우저 | 불가 | 가능 |
    | 커뮤니티 | 매우 큼 | 중간 |

### 🤖 Claude Code로 200% 활용하기

!!! example "🤖 Claude Code 프롬프트 1: 이력서 템플릿"
    ```
    TypeScript + docx 라이브러리로 IT 직무 이력서 템플릿을 만드는 함수를 작성해줘.
    인자는 Resume 타입의 객체 하나. 출력은 Buffer. 한글 문서.
    ```

!!! example "🤖 Claude Code 프롬프트 2: React 다운로드 컴포넌트"
    ```
    React 컴포넌트 <DocxDownloader data={...} />를 만들어줘. 클릭하면
    docx 라이브러리로 Word 파일을 생성하고 file-saver로 다운로드해.
    ```

!!! example "🤖 Claude Code 프롬프트 3: 표 동적 생성"
    ```
    2차원 배열을 받아서 docx Table을 생성하는 유틸 함수를 작성해줘.
    첫 행은 자동으로 bold 헤더, 짝수 행은 연한 회색 배경.
    ```

### 🚨 자주 발생하는 에러 Top 3

!!! danger "🚨 에러 1: `Packer.toBuffer is not a function`"
    **원인**: 버전 불일치 또는 import 경로 오류
    **해결**: `npm install docx@latest` 후 `import { Packer } from 'docx'`

!!! danger "🚨 에러 2: 브라우저에서 Buffer is not defined"
    **원인**: Node.js 전용 API를 브라우저에서 사용
    **해결**: `Packer.toBlob()` 사용 (브라우저용)

!!! danger "🚨 에러 3: 한글 줄바꿈 문제"
    **해결**: 문단 구분은 꼭 **별도의 Paragraph**로 (`\n`은 무시됨)

### 📚 학습 체크리스트

- [ ] Node.js에서 기본 Word 생성
- [ ] 표 포함 문서 생성
- [ ] 브라우저에서 다운로드 (Blob)
- [ ] 이력서 템플릿 함수 작성
- [ ] TypeScript 타입 활용

---

## 🎯 4-3 섹션을 마치며

JavaScript 생태계는 **"브라우저에서 직접 문서 생성"**이라는 독보적인 장점이 있어요. React/Next.js 포트폴리오에 "Excel/Word/PDF 다운로드 기능"을 붙이는 건 면접관에게 강한 인상을 남깁니다.

자, 이제 진짜 재미있는 부분이 남았어요. 다음 [4-4. 문서 자동화 파이프라인](04-pipeline.md)에서는 **이 가이드북 자체를 직접 빌드**해볼 겁니다.
