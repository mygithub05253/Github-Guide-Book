# CLAUDE.md - GitHub 레포지토리 활용 가이드북 프로젝트

## Project Overview
개인 프로젝트: 대학생을 위한 GitHub 레포지토리 활용 가이드북 제작
- 대상: 비전공자 포함 개발자 지망생 (대학생)
- 목표: 10,000+ Stars GitHub 레포지토리의 실전 활용 가이드북 (~200페이지)
- 산출물: Markdown + Word(DOCX) + PDF (문서 자동화 파이프라인으로 생성)
- 메타 접근: 가이드북에서 소개하는 문서 라이브러리로 가이드북 자체를 자동 생성
- 기술 스택: Spring Boot, React, Next.js, Python, Data Analysis
- 진로 방향: 풀스택 개발자 (금융권/공기업 취업 목표)

---

## GSTACK Framework Configuration (Garry Tan's Skill Pack)

GSTACK(github.com/garrytan/gstack)은 YC CEO Garry Tan이 만든 23개 스킬 팩으로,
Claude Code의 역할 기반 워크플로우를 체계화합니다.

### Role Definitions

#### CEO / Strategic Planning
- `/office-hours` - 프로젝트 전략 상담, 우선순위 결정
- `/plan-ceo-review` - CEO 관점 계획 리뷰, 비즈니스 임팩트 평가

#### Engineer / Development
- `/plan-eng-review` - 엔지니어링 관점 기술 계획 리뷰
- `/review` - 코드 리뷰 (품질, 패턴, 성능)
- `/think` - 깊은 기술적 사고, 아키텍처 분석

#### Designer / UX
- `/design-consultation` - 디자인 컨설팅, UX 전략
- `/design-review` - 디자인 리뷰, UI/UX 피드백

#### QA / Quality Assurance
- `/qa` - 종합 품질 보증 (코드 + 테스트)
- `/qa-only` - 테스트만 집중 실행

#### Release / Deployment
- `/ship` - 배포 준비 및 실행
- `/land-and-deploy` - 안전한 랜딩 및 배포
- `/canary` - 카나리 배포 전략

#### Security
- `/cso` - 보안 최고 책임자 관점 리뷰

#### Documentation
- `/document-release` - 릴리스 문서화
- `/retro` - 회고 문서 작성

### GSTACK Workflow for This Project

```
[계획 단계]
1. /office-hours → 가이드북 전체 구조 전략 수립
2. /plan-ceo-review → 카테고리 우선순위 및 가치 평가
3. /plan-eng-review → 기술적 실현 가능성 검토

[실행 단계]
4. /think → 각 레포지토리 심층 분석
5. Sequential Thinking → 단계별 논리적 콘텐츠 구성
6. Plan Mode → 변경사항 미리보기 후 적용

[품질 단계]
7. /qa → 콘텐츠 정확성 및 코드 예제 검증
8. /review → 가이드북 품질 리뷰
9. /cso → 보안 관련 레포 가이드 검증

[배포 단계]
10. /document-release → 최종 문서 정리
11. /ship → .md + .docx 최종 산출물 배포
```

---

## Sequential Thinking Integration

Sequential Thinking MCP는 복잡한 분석 작업을 단계별로 수행합니다.

### 활용 시나리오
- 레포지토리 분석: 기능 → 설치 → 사용법 → 실전 예제 순서
- 카테고리 구성: 대분류 → 중분류 → 소분류 논리적 전개
- 코드 예제 작성: 요구사항 → 설계 → 구현 → 테스트 순서

### 병렬 작업 전략
```
Agent 1: Framework/Language 카테고리 상세 작성
Agent 2: Project/Competition 카테고리 상세 작성
Agent 3: Document Libraries 카테고리 상세 작성
Agent 4: MCP Ecosystem + GSTACK 카테고리 상세 작성
→ 최종 통합 및 품질 검증
```

---

## Project Structure

```
PLAF/
├── CLAUDE.md                     # 이 파일 (프로젝트 설정)
├── src/                          # 가이드북 마크다운 원본 (모듈별)
│   ├── 00_introduction.md        # Part 0: 소개 + 메타 컨셉
│   ├── 01_foundation.md          # Part 1: 기초 (비전공자 가이드)
│   ├── 02_frameworks.md          # Part 2: 프레임워크/언어별 학습
│   ├── 03_projects.md            # Part 3: 프로젝트/공모전
│   ├── 04_document_libraries.md  # Part 4: 문서 처리 라이브러리 (핵심)
│   ├── 05_ai_tools.md            # Part 5: AI 개발 도구 (MCP + GSTACK)
│   ├── 06_career.md              # Part 6: 취업 준비/면접
│   └── appendix.md               # 부록
├── scripts/                      # 문서 자동화 파이프라인
│   ├── requirements.txt
│   ├── build_guidebook.py        # 메인 빌드 스크립트
│   ├── md_merger.py              # MD 병합 + 목차 생성
│   ├── md_to_docx.py             # MD → DOCX (python-docx)
│   ├── md_to_pdf.py              # MD → PDF (WeasyPrint)
│   ├── style_config.py           # 공통 스타일 설정
│   └── guidebook.css             # PDF용 CSS
├── output/                       # 자동 생성 산출물
│   ├── Guidebook.md
│   ├── Guidebook.docx
│   └── Guidebook.pdf
└── legacy/                       # 기존 버전 보관
```

---

## Document Guidelines

### 가이드북 구조 (7개 파트 + 부록) — 학습 흐름 최적화
0. **소개** - 가이드북 사용법, 메타 컨셉(문서 라이브러리로 가이드북 자체 생성)
1. **기초 (비전공자 가이드)** - CS 기초, 코딩 입문, Git 기초 → 초보자가 먼저 읽도록 배치
2. **프레임워크/언어별 학습 레포** - Spring Boot, React, Next.js, Django, Node.js 등
3. **프로젝트/공모전 레포** - 실전 프로젝트, 포트폴리오, 해커톤
4. **문서 처리 라이브러리 (핵심)** - Python/Java/JS 문서 라이브러리 + 빌드 파이프라인 실전 예제
5. **AI 개발 도구** - Claude Code MCP 생태계 + GSTACK 워크플로우 통합
6. **취업 준비/면접** - 기술 면접, 포트폴리오, 이력서 전략

### 부록
- A. 추천 학습 로드맵
- B. 유용한 리소스 링크 모음
- C. 가이드북 빌드 파이프라인 사용법

### 레포지토리별 필수 포함 항목
- 레포 개요 및 Stars 수
- 설치 방법 (Installation)
- 기본 사용법 코드 예제
- 실전 활용 시나리오
- Claude Code 연동 팁 (해당시)
- 관련 레포 추천

---

## Quality Standards
- 코드 예제는 실행 가능한 수준으로 작성
- 한국어 설명 + 영어 기술 용어 병행
- 각 레포지토리 최소 1-2페이지 분량
- 최종 산출물: .md (마크다운) + .docx (Word 문서) + .pdf (PDF)
- 빌드 명령: `python scripts/build_guidebook.py`

---

## Tech Stack References
- **Backend**: Spring Boot, Spring Security, JPA/Hibernate
- **Frontend**: React, Next.js, TypeScript, Tailwind CSS
- **Data**: Python, Pandas, Scikit-learn, Streamlit
- **DevOps**: Docker, GitHub Actions, CI/CD
- **AI/ML**: TensorFlow, PyTorch, LangChain
- **Tools**: Claude Code, MCP Servers, GSTACK
