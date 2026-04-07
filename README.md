# GitHub 인기 레포지토리 & AI 개발 도구 완전 활용 가이드북

대학생 개발자 지망생을 위한 **실전 매뉴얼**입니다. 단순한 정보 나열이 아니라, 클론부터 실행, 트러블슈팅, Claude Code 활용 프롬프트까지 "옆에서 선배가 과외해주듯" 따라할 수 있는 단계별 가이드입니다.

## 특징

- **10,000+ Stars** GitHub 레포지토리 35개 이상 실전 가이드
- **7개 파트, 39개 페이지**: 좌측 사이드바 네비게이션으로 탐색
- **15분 퀵스타트** + **Expected Output** + **자주 발생하는 에러 Top 3** + **Claude Code 프롬프트 박스** 표준 구조
- **MkDocs Material** 기반 정적 웹사이트 (검색·다크모드·코드 복사 버튼·Korean i18n)
- **메타 접근**: 가이드북에서 소개하는 도구(`mkdocs-material`, `python-docx`)로 가이드북 자체를 빌드

## 산출물 3종

| 형식 | 빌드 명령 | 용도 |
| --- | --- | --- |
| **웹사이트** | `mkdocs serve` (로컬) / `mkdocs build` (정적) | 검색·다크모드·코드 복사가 필요한 일상 학습용 |
| **PDF** | `mkdocs build` (mkdocs-with-pdf 활성화 시) | 오프라인·인쇄용 |
| **Word(.docx)** | `python scripts/build_guidebook.py` | 편집·인쇄·공유용 |

## 빠른 시작 (5분)

```bash
# 1. 레포지토리 클론
git clone https://github.com/mygithub05253/Github-Guide-Book.git
cd Github-Guide-Book

# 2. 의존성 설치
pip install -r scripts/requirements.txt

# 3. 로컬 미리보기 (http://127.0.0.1:8000)
mkdocs serve

# 4. 정적 사이트 빌드 (site/ 디렉토리에 생성)
mkdocs build

# 5. (선택) DOCX 빌드
PYTHONIOENCODING=utf-8 python scripts/build_guidebook.py
```

## 프로젝트 구조

```
PLAF/
├── docs/                          # 가이드북 원고 (39개 페이지, mkdocs 입력)
│   ├── index.md                   # 가이드북 홈
│   ├── part1-foundation/          # Part 1: 개발 기초 (4페이지)
│   ├── part2-frameworks/          # Part 2: Spring Boot/React/Next.js (5페이지)
│   ├── part3-projects/            # Part 3: 프로젝트/공모전 (4페이지)
│   ├── part4-document-libraries/  # Part 4: 문서 라이브러리 (5페이지)
│   ├── part5-ai-tools/            # Part 5: Claude Code MCP + GSTACK (10페이지)
│   ├── part6-career/              # Part 6: 취업 준비 (3페이지)
│   └── appendix/                  # 부록 A~E (6페이지)
├── src/                           # 원본 마크다운 (legacy, DOCX 빌드용 보존)
├── scripts/                       # 빌드 파이프라인
│   ├── build_guidebook.py         # DOCX 전용 빌드 (구 통합 스크립트)
│   ├── md_merger.py               # src/*.md 병합 + 목차 생성
│   ├── md_to_docx.py              # MD → DOCX (python-docx)
│   ├── md_to_pdf.py               # MD → PDF (legacy, WeasyPrint)
│   ├── format.sh                  # prettier + markdownlint + mkdocs strict 검증
│   ├── style_config.py
│   └── requirements.txt
├── mkdocs.yml                     # MkDocs Material 설정
├── .prettierrc                    # 마크다운 자동 포맷팅 규칙
├── .markdownlint.json             # 마크다운 린팅 규칙 (한국어 친화)
├── .github/workflows/deploy.yml   # GitHub Pages 자동 배포
├── output/                        # DOCX/PDF 산출물 (build_guidebook.py)
└── site/                          # mkdocs build 산출물 (정적 웹사이트)
```

## 빌드 파이프라인

```
[원고] docs/**/*.md
   │
   ├──── mkdocs serve / mkdocs build ────► site/  (정적 웹사이트 + 검색 인덱스)
   │                                          │
   │                                          └──► gh-pages (GitHub Pages 자동 배포)
   │
   └──── (legacy) src/*.md ──► build_guidebook.py ──► output/Guidebook.docx
```

## 집필 자동화 툴킷

| 도구 | 역할 | 설치 |
| --- | --- | --- |
| `mkdocs-material` | 웹사이트 빌드 + 테마 | `pip install mkdocs-material` |
| `mkdocs-with-pdf` | 단일 PDF 동시 출력 | `pip install mkdocs-with-pdf` |
| `pymdown-extensions` | admonition·tabs·tasklist | `pip install pymdown-extensions` |
| `prettier` | 마크다운/코드 자동 포맷팅 | `npm install -g prettier` |
| `markdownlint-cli` | 마크다운 문법 검수 | `npm install -g markdownlint-cli` |
| **Fetch MCP** | GitHub README를 Claude 컨텍스트로 직접 가져오기 | `claude mcp add fetch -s local -- uvx mcp-server-fetch` |
| **Sequential Thinking MCP** | 목차/논리 구조 검증 | `claude mcp add sequential-thinking -s local -- npx -y @modelcontextprotocol/server-sequential-thinking` |

## 자동화 워크플로우

```bash
# 1. 원고 작성 후 자동 포맷팅 + 린팅 + strict 빌드
bash scripts/format.sh

# 2. 로컬에서 결과 확인
mkdocs serve

# 3. main 브랜치에 푸시 → GitHub Actions가 gh-pages에 자동 배포
git push origin main
```

## 사용 도구

- **Claude Code** Plan 모드 + Sequential Thinking + Fetch MCP
- **GSTACK** (Garry Tan's Skill Pack) 워크플로우
- **MkDocs Material** — 정적 사이트 생성
- **python-docx** — Word 문서 생성
- **Prettier + markdownlint** — 원고 품질 자동 검수

## 라이선스

MIT
