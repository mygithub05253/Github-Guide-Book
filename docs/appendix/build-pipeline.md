# 부록 E: 가이드북 빌드 파이프라인 사용법

> 이 가이드북을 **직접 빌드**하거나, **자기 프로젝트의 문서**를 비슷하게 자동화하고 싶을 때 읽으세요.

---

## E-1. 파이프라인 전체 구조

```text
docs/*.md                     ← 원본 (MkDocs Material)
     ↓
┌────────────────────────────┐
│  mkdocs serve / build      │ → site/ (정적 웹사이트)
└────────────────────────────┘
     ↓
     또는
     ↓
src/*.md (섹션별 원본)
     ↓
┌────────────────────────────┐
│ scripts/build_guidebook.py │
└────────────────────────────┘
     ↓
┌─────────────┬──────────────┐
↓             ↓              ↓
md_merger.py  md_to_docx.py  md_to_pdf.py
     ↓             ↓              ↓
Guidebook.md  Guidebook.docx Guidebook.pdf
                  (output/ 디렉토리)
```

---

## E-2. 사전 준비

### Python 3.10 이상

```bash
python --version
```

3.9 이하면 WeasyPrint 의존성 설치에서 막힙니다.

### 가상환경

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate
```

### 의존성 설치

```bash
pip install -r scripts/requirements.txt
```

!!! danger "🚨 자주 발생하는 에러: WeasyPrint 설치 실패 (Windows)"
    - **원인:** GTK3 라이브러리 누락
    - **해결:** [GTK3 Runtime](https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases) 설치 후 재시도
    - **대안:** PDF 생성을 건너뛰려면 `scripts/build_guidebook.py`에서 `md_to_pdf` 단계 주석 처리

---

## E-3. MkDocs 웹사이트 빌드

### 개발 서버 (실시간 미리보기)

```bash
mkdocs serve
```

!!! info "예상 출력"
    ```text
    INFO    -  Building documentation...
    INFO    -  Documentation built in 1.23 seconds
    INFO    -  [12:34:56] Serving on http://127.0.0.1:8000/
    ```

`docs/*.md` 파일을 저장할 때마다 자동 리로드됩니다.

### 정적 사이트 빌드

```bash
mkdocs build
```

`site/` 디렉토리에 정적 HTML이 생성됩니다. 이것을 GitHub Pages, Netlify, Vercel 등에 그대로 업로드할 수 있습니다.

### 테마 커스터마이즈

`mkdocs.yml` 예시:

```yaml
site_name: GitHub 인기 레포지토리 가이드북
theme:
  name: material
  language: ko
  palette:
    - scheme: default
      primary: indigo
      accent: pink
  features:
    - navigation.tabs
    - navigation.sections
    - content.code.copy
    - content.code.annotate

markdown_extensions:
  - admonition
  - pymdownx.details
  - pymdownx.superfences
  - pymdownx.highlight
  - attr_list
  - tables
```

!!! tip "💡 꿀팁: Material 테마의 admonition"
    `!!! tip`, `!!! warning`, `!!! example` 같은 콜아웃은 Material 테마의 핵심 기능입니다. 이 가이드북 전체가 이 기능으로 구성되어 있습니다.

---

## E-4. DOCX / PDF 빌드

### 원샷 빌드

```bash
python scripts/build_guidebook.py
```

산출물:
- `output/Guidebook.md` (병합된 단일 마크다운)
- `output/Guidebook.docx` (Word)
- `output/Guidebook.pdf`

### 개별 실행

```bash
# 병합만
python scripts/md_merger.py

# DOCX만
python scripts/md_to_docx.py

# PDF만
python scripts/md_to_pdf.py
```

### 스타일 커스터마이즈

- DOCX: `scripts/style_config.py` 수정
- PDF: `scripts/guidebook.css` 수정

!!! example "🤖 Claude Code 프롬프트: 스타일 변경"
    ```
    scripts/guidebook.css 를 열어서
    본문 폰트를 Noto Sans KR로 바꾸고,
    코드 블록 배경을 #f5f5f5 로 변경해줘.
    Plan 모드로 미리 보여줘.
    ```

---

## E-5. GitHub Actions 자동 배포

`.github/workflows/deploy.yml` 예시:

```yaml
name: Deploy Guidebook

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          pip install -r scripts/requirements.txt

      - name: Build MkDocs site
        run: mkdocs build

      - name: Build DOCX + PDF
        run: python scripts/build_guidebook.py

      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./site

      - name: Upload artifacts
        uses: actions/upload-artifact@v4
        with:
          name: guidebook-outputs
          path: output/
```

이렇게 해두면 `main` 브랜치에 push할 때마다:
1. MkDocs 사이트가 GitHub Pages에 자동 배포
2. DOCX/PDF가 GitHub Actions 아티팩트로 업로드

!!! warning "⚠️ 주의: GitHub Pages 활성화 필요"
    Repository → Settings → Pages → Source: `gh-pages` branch 설정이 먼저 필요합니다.

---

## E-6. 파이프라인 확장하기

### 아이디어 1: 다국어 지원
```bash
# mkdocs-i18n 플러그인
pip install mkdocs-static-i18n
```

### 아이디어 2: 검색 강화
```yaml
plugins:
  - search:
      lang: ko
```

### 아이디어 3: PDF에 목차 + 표지
`scripts/guidebook.css` 에 `@page` 규칙 추가:

```css
@page {
  size: A4;
  margin: 2.5cm 2cm;
  @top-right { content: counter(page); }
}

@page :first {
  @top-right { content: none; }
}
```

### 아이디어 4: 코드 블록 line numbers
`mkdocs.yml`:
```yaml
markdown_extensions:
  - pymdownx.highlight:
      linenums: true
```

---

## E-7. 흔한 문제 해결

!!! danger "🚨 `mkdocs: command not found`"
    - **원인:** 가상환경 미활성화 또는 PATH 문제
    - **해결:** `python -m mkdocs serve` 형태로 실행

!!! danger "🚨 PDF 한글이 깨져요"
    - **원인:** WeasyPrint 기본 폰트에 한글 없음
    - **해결:** `guidebook.css` 에 `@font-face` 로 Noto Sans KR 등록

!!! danger "🚨 이미지가 PDF에 안 나와요"
    - **원인:** 상대 경로 문제
    - **해결:** 이미지를 `docs/assets/` 에 두고 절대 경로 참조

---

## E-8. 기여 방법

이 가이드북은 오픈소스입니다. 오타 수정, 예제 추가, 번역 등 어떤 기여든 환영합니다.

1. Fork
2. Branch (`fix/typo-part5`)
3. Commit (한국어 커밋 메시지 OK)
4. PR 생성

!!! tip "💡 꿀팁: 기여 전 Plan 모드"
    큰 변경은 PR 전에 이슈로 먼저 논의하세요. `/plan-ceo-review`로 변경의 가치를 먼저 검증하는 것도 좋습니다.

---

## 체크리스트

- [ ] Python 3.10 이상 확인
- [ ] `mkdocs serve`로 로컬 미리보기 성공
- [ ] `python scripts/build_guidebook.py`로 DOCX/PDF 생성 성공
- [ ] `mkdocs.yml` 테마 옵션을 한 번 수정해봤다
- [ ] GitHub Actions 워크플로우 템플릿을 이해했다

---

## 마치며

이 부록을 끝까지 읽었다면, 이제 당신은:

1. **이 가이드북을 직접 빌드**할 수 있고
2. **자기 프로젝트의 문서**를 같은 방식으로 자동화할 수 있고
3. **GitHub Actions**로 무료 자동 배포까지 걸 수 있습니다

가이드북이 소개한 라이브러리들로 가이드북 자체를 만드는 **메타 순환**이 완성된 것이죠. Happy documenting!
