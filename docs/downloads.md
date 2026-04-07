# 💾 오프라인 가이드북 다운로드

태블릿·전자책 리더·오프라인 환경에서도 학습할 수 있도록 **PDF**와 **Word(DOCX)** 버전을 제공합니다. 두 파일 모두 `main` 브랜치 푸시 시 [GitHub Actions 파이프라인](https://github.com/mygithub05253/Github-Guide-Book/actions)에서 자동으로 최신 상태로 갱신됩니다.

[:material-file-pdf-box: PDF 버전 다운로드](assets/downloads/Guidebook.pdf){ .md-button .md-button--primary }
[:material-file-word-box: Word(DOCX) 버전 다운로드](assets/downloads/Guidebook.docx){ .md-button }

---

## 📋 빌드 방식

- **원본**: `src/*.md` (총 8개 파트) → `scripts/md_merger.py`로 통합
- **DOCX 변환**: `scripts/md_to_docx.py` (python-docx, 맑은 고딕 · D2Coding)
- **PDF 변환**: `scripts/md_to_pdf.py` (WeasyPrint + `scripts/guidebook.css`)
- **오케스트레이션**: `python scripts/build_guidebook.py --format all`

자세한 빌드 파이프라인 구조는 [부록 E · 빌드 파이프라인](appendix/build-pipeline.md)과 [Part 4-4 · 자동화 파이프라인](part4-document-libraries/04-pipeline.md)을 참조하세요.

!!! info "메타 컨셉"
    이 가이드북은 **스스로를 자동 생성**합니다. Part 4에서 소개하는 문서 처리 라이브러리(python-docx, WeasyPrint 등)가 실제로 이 PDF/DOCX 파일을 만들어냅니다. 본문을 읽고 → 스크립트를 실행 → 결과물을 여기서 다운로드하는 흐름 자체가 학습 경험입니다.
