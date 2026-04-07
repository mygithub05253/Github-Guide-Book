# GitHub 레포지토리 활용 가이드북

대학생 개발자 지망생을 위한 GitHub 인기 레포지토리 실전 활용 가이드북입니다.

## 특징

- **10,000+ Stars** 레포지토리 중심의 실전 가이드
- **7개 파트**: 기초 → 프레임워크 → 프로젝트 → 문서 라이브러리 → AI 도구 → 취업
- **메타 접근**: 가이드북에서 소개하는 문서 라이브러리(python-docx, WeasyPrint)로 **가이드북 자체를 자동 생성**
- **3가지 산출물**: Markdown + Word(DOCX) + PDF

## 빌드 방법

```bash
# 의존성 설치
pip install -r scripts/requirements.txt

# WeasyPrint PDF 생성을 위해 GTK 필요 (Windows)
# MSYS2 설치 후: pacman -S mingw-w64-x86_64-gtk3

# 전체 빌드 (MD + DOCX + PDF)
python scripts/build_guidebook.py

# 특정 포맷만 빌드
python scripts/build_guidebook.py --format md
python scripts/build_guidebook.py --format docx
python scripts/build_guidebook.py --format pdf
```

## 프로젝트 구조

```
PLAF/
├── src/                   # 가이드북 마크다운 원본 (8개 파일)
│   ├── 00_introduction.md # 소개 + 메타 컨셉
│   ├── 01_foundation.md   # 기초 (비전공자 가이드)
│   ├── 02_frameworks.md   # 프레임워크/언어 학습
│   ├── 03_projects.md     # 프로젝트/공모전
│   ├── 04_document_libraries.md  # 문서 처리 라이브러리 (핵심)
│   ├── 05_ai_tools.md     # AI 도구 (MCP + GSTACK)
│   ├── 06_career.md       # 취업 준비
│   └── appendix.md        # 부록
├── scripts/               # 문서 자동화 파이프라인
│   ├── build_guidebook.py # 메인 빌드 스크립트
│   ├── md_merger.py       # MD 병합 + 목차 생성
│   ├── md_to_docx.py      # MD → DOCX (python-docx)
│   ├── md_to_pdf.py       # MD → PDF (WeasyPrint)
│   ├── style_config.py    # 스타일 설정
│   └── guidebook.css      # PDF CSS
├── output/                # 생성 산출물
└── legacy/                # 기존 버전
```

## 빌드 파이프라인

```
src/*.md → md_merger.py → output/Guidebook.md
                              ↓
                    ┌─────────┴─────────┐
                    ↓                   ↓
              md_to_docx.py       md_to_pdf.py
                    ↓                   ↓
           output/Guidebook.docx  output/Guidebook.pdf
```

## 사용 도구

- **Claude Code** Plan 모드 + Sequential Thinking
- **GSTACK** (Garry Tan's Skill Pack) 워크플로우
- **python-docx** — Word 문서 생성
- **WeasyPrint** — PDF 생성
- **Pygments** — 코드 구문 강조

## 기술 스택

Backend: Spring Boot, Django, Express | Frontend: React, Next.js | Data: Python, Pandas | AI: Claude Code, MCP
