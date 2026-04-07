# GitHub 인기 레포지토리 & AI 개발 도구 완전 활용 가이드북

> **대상:** 대학생 개발자 (비전공자 포함, 풀스택 개발자 지망)
>
> **기준:** GitHub Stars 10,000+ 레포지토리 중심
>
> **도구:** Claude Code + GSTACK + Sequential Thinking + Plan 모드 활용
>
> **버전:** 4.0 (구조 개선 + 자동화 파이프라인)

---

## 이 가이드북에 대하여

이 가이드북은 **대학생 개발자 지망생**을 위한 실전 GitHub 레포지토리 활용서입니다.

단순히 "이런 레포가 있다"를 넘어, **각 레포지토리를 어떻게 설치하고, 어떻게 사용하고, 실전에서 어떻게 활용하는지**를 코드 예제와 함께 상세히 다룹니다.

### 메타 접근: 가이드북이 스스로를 증명합니다

이 가이드북의 특별한 점은 **Part 4에서 소개하는 문서 처리 라이브러리들로 이 가이드북 자체가 자동 생성된다**는 것입니다.

```
src/*.md  →  md_merger.py  →  output/Guidebook.md
                                    ↓
                          ┌─────────┴─────────┐
                          ↓                   ↓
                    md_to_docx.py       md_to_pdf.py
                          ↓                   ↓
                 output/Guidebook.docx  output/Guidebook.pdf
```

- **python-docx** (Part 4-1)로 Word 문서를 자동 생성
- **WeasyPrint** (Part 4-4 확장)로 PDF를 자동 생성
- **Pygments**로 코드 구문 강조를 적용

즉, "이 라이브러리로 이런 걸 만들 수 있다"를 **이 가이드북 자체가 증명**합니다.

---

## 가이드북 구조

| 파트 | 제목 | 대상 | 핵심 내용 |
|------|------|------|-----------|
| **Part 1** | 개발 기초 다지기 | 비전공자/입문자 | CS 기초, 코딩 입문, 데이터 분석 |
| **Part 2** | 프레임워크/언어별 학습 | 초급~중급 | Spring Boot, React, Next.js, Django 등 |
| **Part 3** | 프로젝트 및 공모전 | 중급 | 풀스택 프로젝트, 포트폴리오, 오픈소스 기여 |
| **Part 4** | 문서 처리 라이브러리 | 중급~고급 | python-docx, openpyxl, WeasyPrint 등 |
| **Part 5** | AI 개발 도구 | 모든 레벨 | Claude Code MCP, GSTACK 워크플로우 |
| **Part 6** | 취업 준비/면접 | 취준생 | 기술 면접, 금융/공기업 전략 |
| **부록** | 참고 자료 | 모든 레벨 | 로드맵, 리소스, 빌드 가이드 |

### 추천 읽기 순서

**완전 초보자:** Part 1 → Part 2 → Part 3 → Part 6

**프로그래밍 경험자:** Part 2 → Part 3 → Part 4 → Part 5

**취업 준비생:** Part 6 → Part 3 → Part 4

**AI 도구에 관심:** Part 5 → Part 4 → Part 2

---

## 사용된 도구

### Claude Code Plan 모드
이 가이드북의 구조 설계에 Plan 모드를 활용했습니다. 변경사항을 미리 검토하고 승인 후 적용하는 워크플로우로, 대규모 프로젝트에서 실수를 방지합니다.

### Sequential Thinking
각 레포지토리 분석을 단계별로 수행했습니다:
1. 레포지토리 개요 파악
2. 설치 및 환경 설정
3. 기본 사용법 코드 작성
4. 실전 활용 시나리오 설계
5. 관련 레포지토리 연결

### GSTACK (Garry Tan's Skill Pack)
가이드북 제작 전 과정에서 GSTACK 스킬을 활용했습니다:
- `/office-hours` → 전체 구조 전략 수립
- `/plan-ceo-review` → 파트별 가치 평가
- `/plan-eng-review` → 파이프라인 아키텍처 리뷰
- `/qa` → 콘텐츠 품질 검증
- `/ship` → 최종 산출물 배포

---

## 빠른 시작

```bash
# 이 가이드북을 직접 빌드해보세요!
git clone <repository-url>
cd PLAF

# 의존성 설치
pip install -r scripts/requirements.txt

# 가이드북 빌드 (MD + DOCX + PDF)
python scripts/build_guidebook.py
```

산출물은 `output/` 디렉토리에 생성됩니다.

---
