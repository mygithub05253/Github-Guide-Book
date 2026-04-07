# 4-4. 문서 자동화 파이프라인 — 이 가이드북 직접 빌드하기

> 여기가 이 가이드북의 **하이라이트**입니다. 지금까지 배운 라이브러리들을 조합해서, **이 가이드북 자체를 당신의 이름으로 다시 빌드**해봅니다. 다 끝나고 나면 당신 컴퓨터에 "본인 이름이 박힌 PDF 가이드북"이 하나 생겨있을 거예요.

---

## 🪞 메타 컨셉 다시 짚기

```
src/*.md (원본 마크다운)
    ↓
scripts/md_merger.py       (Part 0 ~ Appendix 병합 + 목차 생성)
    ↓
Guidebook.md               (통합 마크다운)
    ├→ scripts/md_to_docx.py  (python-docx)   → Guidebook.docx
    └→ scripts/md_to_pdf.py   (WeasyPrint)    → Guidebook.pdf
```

이 섹션의 모든 코드는 이 가이드북의 실제 `scripts/` 폴더에서 확인할 수 있어요.

---

## 📋 이 섹션에서 배울 수 있는 것

- 마크다운 여러 파일 병합
- 마크다운 → DOCX 변환
- 마크다운 → PDF 변환
- CLI 빌드 스크립트 구조
- 당신 이름이 박힌 개인화된 가이드북 생성

---

## 🚀 미니 튜토리얼: 5분 안에 내 이름이 박힌 PDF 만들기

### Step 1: 프로젝트 클론

```bash
git clone https://github.com/<your-github>/PLAF.git
cd PLAF
```

!!! warning "⚠️ 주의"
    아직 이 프로젝트를 로컬에 받지 않았다면, 먼저 clone부터 해주세요. 이 튜토리얼은 `scripts/` 폴더가 있는 PLAF 프로젝트 루트에서 실행합니다.

### Step 2: 의존성 설치

```bash
python -m venv venv
source venv/bin/activate        # macOS/Linux
# venv\Scripts\activate          # Windows

pip install -r scripts/requirements.txt
```

!!! info "예상 출력"
    ```
    Successfully installed python-docx-1.1.0 markdown-3.5.2 weasyprint-60.2 ...
    ```

### Step 3: 표지 정보 커스터마이징

`scripts/style_config.py` 파일을 열어 표지의 저자 이름을 본인으로 수정하세요.

```python
COVER_AUTHOR = "홍길동"          # ← 본인 이름으로 변경
COVER_SUBTITLE = "나만의 개인 가이드북"
COVER_DATE = "2026-04-07"
```

### Step 4: 빌드 실행

```bash
python scripts/build_guidebook.py
```

!!! info "예상 출력"
    ```
    [1/3] 마크다운 병합 중...
    [2/3] DOCX 생성 중...
    [3/3] PDF 생성 중...
    ✔ output/Guidebook.md  (125 KB)
    ✔ output/Guidebook.docx (480 KB)
    ✔ output/Guidebook.pdf  (3.2 MB)
    빌드 완료!
    ```

### Step 5: 결과 확인

`output/` 폴더에 생성된 3개 파일을 각각 열어보세요.

- **Guidebook.md** — 병합된 마크다운 원본
- **Guidebook.docx** — Word에서 편집 가능한 버전
- **Guidebook.pdf** — 출력/공유용 PDF

**표지에 당신 이름이 박혀있나요?** 축하합니다. 이 가이드북은 이제 **당신의 가이드북**이에요.

---

## 🏗 빌드 파이프라인 내부 동작 이해하기

### `build_guidebook.py` 구조

```python
# scripts/build_guidebook.py
from md_merger import merge_markdown
from md_to_docx import convert_to_docx
from md_to_pdf import convert_to_pdf
from style_config import SRC_DIR, OUTPUT_DIR

def main():
    print("[1/3] 마크다운 병합 중...")
    merged_md = merge_markdown(SRC_DIR, OUTPUT_DIR / "Guidebook.md")

    print("[2/3] DOCX 생성 중...")
    convert_to_docx(merged_md, OUTPUT_DIR / "Guidebook.docx")

    print("[3/3] PDF 생성 중...")
    convert_to_pdf(merged_md, OUTPUT_DIR / "Guidebook.pdf")

    print("빌드 완료!")

if __name__ == "__main__":
    main()
```

### `md_merger.py` — 여러 마크다운 파일 합치기

```python
from pathlib import Path

def merge_markdown(src_dir: Path, output: Path) -> Path:
    parts = sorted(src_dir.glob("*.md"))   # 00_introduction.md, 01_foundation.md, ...
    merged = []

    for part in parts:
        content = part.read_text(encoding="utf-8")
        merged.append(content)
        merged.append("\n\n---\n\n")       # 파트 간 구분선

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(merged), encoding="utf-8")
    return output
```

### `md_to_docx.py` — 핵심 변환 로직 (python-docx)

```python
import re
from pathlib import Path
from docx import Document
from docx.shared import Pt, RGBColor
from style_config import COVER_AUTHOR, COVER_SUBTITLE, COVER_DATE

def convert_to_docx(md_path: Path, output: Path) -> Path:
    doc = Document()

    # 표지
    doc.add_heading("GitHub 레포지토리 활용 가이드북", level=0)
    doc.add_paragraph(COVER_SUBTITLE)
    doc.add_paragraph(f"저자: {COVER_AUTHOR}")
    doc.add_paragraph(f"작성일: {COVER_DATE}")
    doc.add_page_break()

    # 본문
    md_text = md_path.read_text(encoding="utf-8")
    for line in md_text.splitlines():
        if line.startswith("# "):
            doc.add_heading(line[2:], level=1)
        elif line.startswith("## "):
            doc.add_heading(line[3:], level=2)
        elif line.startswith("### "):
            doc.add_heading(line[4:], level=3)
        elif line.startswith("```"):
            continue        # 코드 블록 간단 처리
        elif line.strip():
            doc.add_paragraph(line)

    doc.save(output)
    return output
```

!!! tip "💡 실전 팁"
    위 파서는 **단순화된 버전**이에요. 실제 `scripts/md_to_docx.py`는 인라인 코드(`` ` ``), 링크, 표, 이미지까지 처리합니다. 하지만 핵심 원리는 같아요. **"마크다운 한 줄씩 읽고 → python-docx 호출"**이 전부입니다.

### `md_to_pdf.py` — WeasyPrint로 PDF 변환

```python
from pathlib import Path
import markdown
from weasyprint import HTML, CSS
from style_config import CSS_PATH

def convert_to_pdf(md_path: Path, output: Path) -> Path:
    md_text = md_path.read_text(encoding="utf-8")

    # Markdown → HTML
    html = markdown.markdown(
        md_text,
        extensions=["tables", "fenced_code", "toc"],
    )

    # HTML → PDF
    HTML(string=html).write_pdf(
        output,
        stylesheets=[CSS(filename=str(CSS_PATH))],
    )
    return output
```

### `guidebook.css` — PDF 스타일 (핵심 일부)

```css
@page {
    size: A4;
    margin: 2.5cm 2cm;
    @bottom-center {
        content: counter(page) " / " counter(pages);
    }
}

body {
    font-family: 'NanumGothic', sans-serif;
    font-size: 11pt;
    line-height: 1.6;
}

h1 { color: #1a1a1a; border-bottom: 3px solid #4472C4; padding-bottom: 8px; }
h2 { color: #4472C4; }

code {
    background: #f4f4f4;
    padding: 2px 6px;
    border-radius: 3px;
    font-family: 'Consolas', monospace;
}

pre {
    background: #282c34;
    color: #abb2bf;
    padding: 12px;
    border-radius: 6px;
    overflow-x: auto;
}
```

---

## 🤖 Claude Code로 파이프라인 개선하기

!!! example "🤖 Claude Code 프롬프트 1: 목차 자동 생성"
    ```
    scripts/md_to_docx.py에 "본문 스캔 → 제목 수집 → 표지 다음 페이지에 목차 삽입"
    기능을 추가해줘. python-docx의 add_paragraph로 목차 항목을 작성하고,
    현재 페이지 번호는 일단 생략해도 돼.
    ```

!!! example "🤖 Claude Code 프롬프트 2: 코드 블록 하이라이트"
    ```
    scripts/md_to_pdf.py의 WeasyPrint 변환에서 코드 블록에 Pygments 신택스
    하이라이트가 적용되도록 개선해줘. markdown 확장 `codehilite`를 써.
    ```

!!! example "🤖 Claude Code 프롬프트 3: 개인화 CLI 인자"
    ```
    build_guidebook.py에 --author, --subtitle, --date CLI 인자를 추가해줘.
    argparse 사용. 기본값은 style_config에서 읽어와.
    ```

!!! example "🤖 Claude Code 프롬프트 4: 빌드 속도 측정"
    ```
    각 단계(merge/docx/pdf)의 소요 시간을 측정해서 빌드 종료 시
    "merge: 0.3s, docx: 2.1s, pdf: 4.5s" 형식으로 출력하게 해줘.
    """
```

---

## 💡 실전 활용: 포트폴리오 자동 생성기 만들기

여기서 배운 내용을 응용하면 **GitHub 프로필 → Word 포트폴리오**를 자동 생성할 수 있어요.

```python
import requests
from docx import Document
from docx.shared import Inches

def generate_portfolio(username: str):
    # GitHub API로 Top 10 레포 가져오기
    resp = requests.get(f'https://api.github.com/users/{username}/repos')
    repos = sorted(resp.json(), key=lambda r: r['stargazers_count'], reverse=True)[:10]

    doc = Document()
    doc.add_heading(f'{username}의 GitHub 포트폴리오', 0)
    doc.add_paragraph(f'생성일: 2026-04-07')
    doc.add_paragraph(f'총 {len(repos)}개 대표 프로젝트')

    for repo in repos:
        doc.add_heading(repo['name'], level=1)
        doc.add_paragraph(repo.get('description') or '(설명 없음)')

        p = doc.add_paragraph()
        p.add_run(f"⭐ {repo['stargazers_count']}  ").bold = True
        p.add_run(f"언어: {repo.get('language') or 'N/A'}  ")
        p.add_run(f"🔗 {repo['html_url']}")

    doc.save(f'{username}_portfolio.docx')
    print(f'{username}_portfolio.docx 생성 완료')

generate_portfolio('torvalds')
```

!!! example "🤖 Claude Code 프롬프트: 포트폴리오 확장"
    ```
    위 generate_portfolio 함수를 확장해서 (1) 각 레포의 README 첫 단락을
    GitHub API로 가져와 요약에 넣고 (2) 언어 통계 표를 추가하고
    (3) 최근 1년 contribution 그래프 이미지를 저장 뒤 문서에 삽입하게 해줘.
    ```

---

## 🚨 자주 발생하는 에러 Top 3

!!! danger "🚨 에러 1: `WeasyPrint` 설치 실패 (Windows)"
    **원인**: GTK 라이브러리 의존성 문제
    **해결**:
    1. https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases 에서 GTK 설치
    2. 환경변수 PATH에 GTK 추가
    3. `pip install weasyprint` 재실행

!!! danger "🚨 에러 2: PDF의 한글이 네모로 표시"
    **원인**: `guidebook.css`의 `font-family` 폰트가 시스템에 없음
    **해결**:
    ```css
    body {
        font-family: 'Malgun Gothic', 'NanumGothic', 'Noto Sans CJK KR', sans-serif;
    }
    ```

!!! danger "🚨 에러 3: `PermissionError: [Errno 13] output/Guidebook.docx`"
    **원인**: 이전에 생성한 파일이 Word에서 열려있음
    **해결**: Word 종료 후 재실행

---

## 📚 학습 체크리스트

- [ ] `scripts/requirements.txt` 설치 성공
- [ ] `python scripts/build_guidebook.py` 실행 성공
- [ ] `output/` 폴더에서 3개 파일 모두 확인
- [ ] `style_config.py`에서 본인 이름으로 표지 변경
- [ ] `md_to_docx.py` 코드를 읽고 흐름 이해
- [ ] `md_to_pdf.py` + `guidebook.css` 스타일 1개 이상 수정
- [ ] 본인 GitHub 포트폴리오를 위 예제로 자동 생성
- [ ] Claude Code로 파이프라인 기능 1개 이상 개선

---

## 🎯 Part 4를 마치며

축하합니다. 여기까지 왔다면 당신은 이제:

1. **Word, Excel, PDF, PowerPoint**를 코드로 자유자재로 다룰 수 있고
2. **Java 생태계**(Apache POI, iText)의 차이도 알고
3. **브라우저에서 직접 문서 생성**도 할 줄 알고
4. 무엇보다 **이 가이드북의 내부 동작을 완전히 이해**하는 사람이 되었어요.

이 지점부터는 세상의 거의 모든 "문서 반복 작업"을 자동화할 수 있는 힘을 가진 거예요. 매주 2시간씩 걸리던 보고서 작업이 3초가 되는 경험을 직접 해보세요. 진짜 개발자가 된 느낌이 뭔지 알게 될 겁니다.

!!! tip "💡 Part 4 졸업 과제"
    다음 중 하나를 골라 본인 GitHub에 올려보세요.

    1. **주간 보고서 자동화기** — 매주 월요일 9시에 Git 로그 → Word 보고서
    2. **학점 관리 Excel** — CSV 성적 → 자동 GPA 계산 + 차트
    3. **청구서 발행기** — JSON 데이터 → 한글 PDF 청구서
    4. **이력서 빌더** — YAML 프로필 → Word + PDF 이력서 동시 생성

    어떤 것을 고르든, "하나의 데이터 소스 → 여러 포맷 출력"이라는 파이프라인 설계 경험이 핵심입니다.

다음은 [Part 5: AI 개발 도구](../part5-ai-tools/index.md)에서 Claude Code의 진짜 잠재력인 MCP 생태계와 GSTACK 워크플로우를 다룹니다.
