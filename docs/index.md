# GitHub 인기 레포지토리 & AI 개발 도구 완전 활용 가이드북

> **대상:** 대학생 개발자 (비전공자 포함, 풀스택 개발자 지망)
>
> **기준:** GitHub Stars 10,000+ 레포지토리 중심
>
> **도구:** Claude Code + GSTACK + Sequential Thinking + Plan 모드 활용
>
> **버전:** 5.0 (MkDocs Material 리팩토링 + 초보자 실전 매뉴얼 강화)

---

## 🌐 로드맵 포털: 카테고리별 딥다이브 (NEW)

[roadmap.sh](https://roadmap.sh) 커리큘럼을 기준으로 분야별 핵심 오픈소스 레포지토리를 카드형 UI로 탐색하세요. 각 카드는 **"왜 쓰는가 → 10분 퀵스타트 → 코드 해부학 → AI 프롬프트 팩"** 표준 템플릿을 따릅니다.

<div class="grid cards" markdown>

-   :material-react: __프론트엔드__

    ---

    React, Next.js, Tailwind, Zustand

    [:octicons-arrow-right-24: 카테고리 보기](roadmap/index.md)

-   :material-api: __백엔드__

    ---

    Spring Boot, FastAPI, NestJS, Django, Express

    [:octicons-arrow-right-24: 카테고리 보기](roadmap/index.md)

-   :material-robot-outline: __AI / 데이터__

    ---

    LangChain, AutoGPT, PyTorch, Transformers, Pandas

    [:octicons-arrow-right-24: 카테고리 보기](roadmap/index.md)

-   :material-kubernetes: __DevOps / 클라우드__

    ---

    Kubernetes, Docker, Terraform, Ansible, Prometheus

    [:octicons-arrow-right-24: 카테고리 보기](roadmap/index.md)

-   :simple-postgresql: __DB / 스트리밍__

    ---

    PostgreSQL, Redis, Elasticsearch, Kafka

    [:octicons-arrow-right-24: 카테고리 보기](roadmap/index.md)

-   :material-school: __CS 기초 & 보안__

    ---

    OSSU, Coding Interview University, System Design, OWASP

    [:octicons-arrow-right-24: 카테고리 보기](roadmap/index.md)

</div>

[:material-download: 오프라인 PDF/DOCX 다운로드](downloads.md){ .md-button .md-button--primary }

---

## 이 가이드북을 한 문장으로 요약하면

"**10,000 Stars 이상의 GitHub 레포지토리 중 진짜 쓸 만한 것들을, 비전공자도 바로 따라 할 수 있게 실습 위주로 정리한 선배의 과외 노트**"입니다.

!!! info "📌 핵심 요약"
    - **누구에게:** 개발을 배우고 싶은 대학생 (비전공자 OK)
    - **무엇을:** GitHub 스타 레포지토리 + Claude Code + MCP + GSTACK
    - **어떻게:** 복사 가능한 명령어, 자연어 프롬프트 예시, 실수 포인트 콜아웃
    - **왜:** 혼자 공부하다 막힐 때, 옆에서 "이거 이렇게 하면 돼" 말해주는 선배가 필요하니까

---

## 이 가이드북에 대하여

이 가이드북은 단순히 "이런 레포가 있어요"를 나열하지 않습니다. 각 레포지토리를 **어떻게 설치하고, 어떻게 쓰고, 실전에서 어떻게 조합하는지** 코드와 자연어 프롬프트 예시로 보여줍니다.

특히 요즘 필수가 된 **Claude Code + MCP(Model Context Protocol) + GSTACK 워크플로우**를 중심에 두고, "AI와 함께 개발한다는 건 구체적으로 무엇인가"에 대한 답을 제공합니다.

### 선배가 과외하듯 쓴 이유

!!! tip "💡 꿀팁: 이 가이드북을 읽는 법"
    - 처음엔 **Part 1 → Part 2 순서**로 읽으세요. 모르는 용어가 나오면 일단 넘어가도 됩니다.
    - 각 페이지 위쪽의 "이걸 언제 써야 하는가" 부분만 먼저 훑어봐도 감이 잡힙니다.
    - 코드 블록은 그냥 읽지 말고 **직접 터미널에 복사**해서 돌려보세요. 에러가 나는 게 정상입니다.
    - `!!! danger` 콜아웃은 실제 학생들이 자주 겪는 함정입니다. 꼭 한 번 읽어두세요.

---

## 메타 컨셉: 가이드북이 스스로를 증명합니다

이 가이드북의 가장 재미있는 점은 **Part 4에서 소개하는 문서 처리 라이브러리들로 이 가이드북 자체가 자동 생성된다**는 것입니다.

```text
src/*.md  →  md_merger.py  →  output/Guidebook.md
                                    ↓
                          ┌─────────┴─────────┐
                          ↓                   ↓
                    md_to_docx.py       md_to_pdf.py
                          ↓                   ↓
                 output/Guidebook.docx  output/Guidebook.pdf
```

사용된 기술:

- **python-docx** — Word 문서 자동 생성
- **WeasyPrint** — PDF 생성 (CSS 기반 레이아웃)
- **Pygments** — 코드 구문 강조
- **MkDocs Material** — 이 웹사이트 (지금 보고 있는 화면)

즉, "이 라이브러리로 이런 걸 만들 수 있다"를 **이 가이드북 자체가 살아있는 증거**로 보여줍니다.

!!! example "🤖 Claude Code 프롬프트: 메타 구조 이해하기"
    ```
    이 프로젝트의 scripts/build_guidebook.py 를 읽고,
    md 파일이 docx와 pdf로 변환되는 전체 파이프라인을
    단계별로 설명해줘. 각 단계에서 어떤 라이브러리가 쓰이는지도.
    ```

---

## 가이드북 구조 (7개 파트 + 부록)

| 파트 | 제목 | 대상 | 핵심 내용 |
|------|------|------|-----------|
| **Part 1** | 개발 기초 다지기 | 비전공자/입문자 | CS 기초, Git, 터미널, 에디터 |
| **Part 2** | 프레임워크/언어별 학습 | 초급~중급 | Spring Boot, React, Next.js, Django |
| **Part 3** | 프로젝트 및 공모전 | 중급 | 풀스택 프로젝트, 포트폴리오, 해커톤 |
| **Part 4** | 문서 처리 라이브러리 | 중급~고급 | python-docx, openpyxl, WeasyPrint |
| **Part 5** | AI 개발 도구 | 모든 레벨 | Claude Code MCP, GSTACK 워크플로우 |
| **Part 6** | 취업 준비/면접 | 취준생 | 기술 면접, 금융/공기업 전략 |
| **부록** | 참고 자료 | 모든 레벨 | Plan 모드, Sequential Thinking, 로드맵 |

### 추천 읽기 순서 (상황별)

!!! info "📌 당신이 누구냐에 따라 다릅니다"
    - **완전 초보자:** Part 1 → Part 2 → Part 3 → Part 6
    - **프로그래밍 경험자:** Part 2 → Part 3 → Part 4 → Part 5
    - **취업 준비생:** Part 6 → Part 3 → Part 4 → 부록 C
    - **AI 도구에 관심:** Part 5 → 부록 A/B → Part 4 → Part 2
    - **문서 자동화 관심:** Part 4 → 부록 E → Part 5

---

## 빠른 시작 5분 튜토리얼 — 이 가이드북을 직접 빌드해보기

가이드북을 "읽기만" 하는 건 재미없습니다. 직접 빌드해서 `mkdocs serve`로 띄워보세요. 아래 명령어를 복사해서 터미널에 붙여넣으면 됩니다.

### Step 1: 레포지토리 클론

```bash
git clone https://github.com/mygithub05253/Github-Guide-Book.git
cd Github-Guide-Book
```

!!! warning "⚠️ 주의: Python 3.10 이상 필요"
    `python --version`으로 먼저 확인하세요. 3.9 이하면 WeasyPrint 의존성 설치 단계에서 에러가 납니다.

### Step 2: Python 의존성 설치

```bash
# 가상환경 권장
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate

# 의존성 설치
pip install -r scripts/requirements.txt
```

!!! danger "🚨 자주 발생하는 에러: `pip: command not found`"
    - **원인:** Python이 설치되지 않았거나 PATH에 등록되지 않음
    - **해결:** [python.org](https://www.python.org/downloads/)에서 설치 시 "Add Python to PATH" 체크
    - **Windows 대안:** `py -m pip install -r scripts/requirements.txt`

### Step 3: MkDocs 개발 서버 실행

```bash
mkdocs serve
```

!!! info "예상 출력"
    ```text
    INFO    -  Building documentation...
    INFO    -  Documentation built in 1.23 seconds
    INFO    -  [12:34:56] Watching paths for changes: 'docs', 'mkdocs.yml'
    INFO    -  [12:34:56] Serving on http://127.0.0.1:8000/
    ```

브라우저에서 `http://127.0.0.1:8000`을 열면 지금 읽고 있는 이 웹사이트가 당신의 컴퓨터에서 동작합니다.

### Step 4: DOCX + PDF 산출물 빌드

```bash
python scripts/build_guidebook.py
```

`output/` 디렉토리에 `Guidebook.md`, `Guidebook.docx`, `Guidebook.pdf` 가 생성됩니다.

!!! tip "💡 꿀팁: 실시간 미리보기"
    `mkdocs serve`는 파일을 저장할 때마다 자동으로 리로드됩니다. `docs/` 안의 md 파일을 수정하면서 브라우저로 바로 결과를 확인하세요. 이 작업 흐름만 익혀도 문서 작업 생산성이 3배 오릅니다.

!!! example "🤖 Claude Code 프롬프트: 첫 빌드 에러 해결"
    ```
    지금 mkdocs serve 실행했는데 다음 에러가 떴어:
    [에러 메시지 붙여넣기]
    에러 원인과 해결 방법을 단계별로 알려줘. Windows 환경이야.
    ```

---

## 사용된 도구 요약

### Claude Code
Anthropic의 공식 CLI 코딩 에이전트. 자연어로 명령하면 파일을 읽고 수정하고 테스트까지 돌립니다. 이 가이드북은 Claude Code로 작성되었습니다.

### MCP (Model Context Protocol)
Claude Code가 GitHub, 파일 시스템, DB 등 **외부 도구**와 통신하기 위한 표준 프로토콜. USB에 비유하면 이해하기 쉽습니다 — 어떤 도구든 MCP 케이블 하나로 꽂으면 Claude가 쓸 수 있습니다.

### GSTACK (Garry Tan's Skill Pack)
YC CEO 개리 탄이 만든 23개 스킬 팩. `/office-hours`, `/review`, `/ship` 같은 슬래시 명령어로 CEO/엔지니어/QA/배포 역할을 체계화합니다.

### Plan 모드
변경사항을 **미리 보여준 후** 승인받고 실행하는 안전 장치. `Shift+Tab` 두 번으로 토글합니다. 대규모 리팩토링에 필수.

### Sequential Thinking
복잡한 문제를 단계별로 쪼개서 추론하는 MCP. 알고리즘 설계, 아키텍처 결정, 버그 원인 분석에 강력합니다.

---

## 다음 단계

- **초보자라면** → Part 1부터 차근차근
- **AI 도구가 궁금하다면** → [Part 5 개요](part5-ai-tools/index.md)로 바로 이동
- **설치/환경 문제라면** → [부록 E: 빌드 파이프라인](appendix/build-pipeline.md)
- **로드맵이 필요하면** → [부록 C: 학습 로드맵](appendix/learning-roadmap.md)

!!! tip "💡 마지막 꿀팁"
    **읽는 것보다 직접 해보는 게 10배 빠릅니다.** 각 페이지의 코드 블록을 눈으로만 훑지 마세요. 복사 → 붙여넣기 → 에러 → 구글링 → 해결, 이 사이클을 30번만 돌리면 실력이 달라집니다.
