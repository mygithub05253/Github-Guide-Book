"""
가이드북 빌드 오케스트레이터
MD 병합 → DOCX 변환 → PDF 변환을 순서대로 실행합니다.

사용법:
  python scripts/build_guidebook.py              # 전체 빌드 (MD + DOCX + PDF)
  python scripts/build_guidebook.py --format md   # MD만 빌드
  python scripts/build_guidebook.py --format docx # MD + DOCX
  python scripts/build_guidebook.py --format pdf  # MD + PDF
"""

import argparse
import os
import sys
import time
from pathlib import Path

# Windows에서 WeasyPrint PDF 생성을 위해 MSYS2 GTK 라이브러리 경로 추가
# PATH 뒤에 추가하여 기존 Python 등의 경로를 간섭하지 않도록 함
msys2GtkPath = Path("C:/msys64/mingw64/bin")
if msys2GtkPath.exists() and str(msys2GtkPath) not in os.environ.get("PATH", ""):
  os.environ["PATH"] = os.environ.get("PATH", "") + os.pathsep + str(msys2GtkPath)

# 스크립트 디렉토리를 sys.path에 추가
scriptDir = Path(__file__).parent
sys.path.insert(0, str(scriptDir))

from md_merger import mergeMdFiles
from md_to_docx import convertMdToDocx
from md_to_pdf import generateHtml, convertHtmlToPdf


def parseArgs():
  """CLI 인자 파싱"""
  parser = argparse.ArgumentParser(
    description="GitHub 레포지토리 활용 가이드북 빌드 도구"
  )
  parser.add_argument(
    "--format",
    choices=["md", "docx", "pdf", "all"],
    default="all",
    help="빌드할 포맷 (기본값: all)"
  )
  return parser.parse_args()


def main():
  """메인 빌드 실행"""
  args = parseArgs()
  startTime = time.time()

  projectRoot = scriptDir.parent
  srcDir = projectRoot / "src"
  outputDir = projectRoot / "output"
  mdPath = outputDir / "Guidebook.md"
  docxPath = outputDir / "Guidebook.docx"
  pdfPath = outputDir / "Guidebook.pdf"
  cssPath = scriptDir / "guidebook.css"

  print()
  print("╔" + "═" * 58 + "╗")
  print("║  GitHub 레포지토리 활용 가이드북 - 빌드 시스템         ║")
  print("╠" + "═" * 58 + "╣")
  print(f"║  포맷: {args.format:<51}║")
  print("╚" + "═" * 58 + "╝")
  print()

  # 1단계: MD 병합 (항상 실행)
  print("[1/3] MD 파일 병합...")
  mdContent = mergeMdFiles(srcDir, mdPath)
  if mdContent is None:
    print("\n[실패] MD 병합에 실패했습니다.")
    sys.exit(1)

  # 2단계: DOCX 변환
  if args.format in ("docx", "all"):
    print()
    print("[2/3] DOCX 변환...")
    try:
      convertMdToDocx(mdContent, docxPath)
    except ImportError:
      print("  [경고] python-docx가 설치되어 있지 않습니다.")
      print("  pip install python-docx 를 실행해주세요.")
    except Exception as e:
      print(f"  [오류] DOCX 변환 실패: {e}")
  else:
    print("\n[2/3] DOCX 변환 건너뜀")

  # 3단계: PDF 변환
  if args.format in ("pdf", "all"):
    print()
    print("[3/3] PDF 변환...")
    try:
      html = generateHtml(mdContent, cssPath)
      convertHtmlToPdf(html, pdfPath)
    except ImportError:
      print("  [경고] weasyprint가 설치되어 있지 않습니다.")
      print("  pip install weasyprint 를 실행해주세요.")
    except Exception as e:
      print(f"  [오류] PDF 변환 실패: {e}")
  else:
    print("\n[3/3] PDF 변환 건너뜀")

  # 결과 요약
  elapsed = time.time() - startTime
  print()
  print("╔" + "═" * 58 + "╗")
  print("║  빌드 완료!                                           ║")
  print("╠" + "═" * 58 + "╣")

  for path, label in [(mdPath, "MD"), (docxPath, "DOCX"), (pdfPath, "PDF")]:
    if path.exists():
      size = path.stat().st_size
      if size > 1024 * 1024:
        sizeStr = f"{size / 1024 / 1024:.1f} MB"
      else:
        sizeStr = f"{size / 1024:.1f} KB"
      print(f"║  {label:>4}: {path.name:<35} {sizeStr:>12}  ║")

  print(f"║  소요 시간: {elapsed:.1f}초{' ' * 42}║")
  print("╚" + "═" * 58 + "╝")
  print()


if __name__ == "__main__":
  main()
