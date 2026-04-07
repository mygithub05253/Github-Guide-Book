"""
MD → PDF 변환 스크립트
markdown 라이브러리로 HTML 변환 후, WeasyPrint로 PDF를 생성합니다.
Pygments로 코드 구문 강조를 적용합니다.
"""

import re
from pathlib import Path
import markdown
from pygments.formatters import HtmlFormatter


def preprocessForPdf(mdContent: str) -> str:
  """PDF 변환 전 포맷별 후처리.

  - HTML 주석 `<!-- ... -->` 제거 (markdown 라이브러리가 그대로 출력하는 경우 방지)
  - 목차 앵커 링크는 PDF에서도 클릭 가능하므로 유지
  """
  mdContent = re.sub(r"<!--.*?-->", "", mdContent, flags=re.DOTALL)
  return mdContent


def generateHtml(mdContent: str, cssPath: Path) -> str:
  """마크다운을 HTML로 변환합니다."""
  mdContent = preprocessForPdf(mdContent)

  # markdown 확장 설정
  extensions = [
    "tables",
    "fenced_code",
    "codehilite",
    "toc",
    "nl2br",
    "sane_lists",
  ]

  extensionConfigs = {
    "codehilite": {
      "css_class": "codehilite",
      "guess_lang": True,
      "linenums": False,
    },
    "toc": {
      "permalink": False,
    },
  }

  # 마크다운 → HTML
  htmlBody = markdown.markdown(
    mdContent,
    extensions=extensions,
    extension_configs=extensionConfigs,
    output_format="html5",
  )

  # Pygments CSS
  pygmentsCss = HtmlFormatter(style="default").get_style_defs(".codehilite")

  # 가이드북 CSS
  guidebookCss = ""
  if cssPath.exists():
    guidebookCss = cssPath.read_text(encoding="utf-8")

  # 완전한 HTML 문서 생성
  html = f"""<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>GitHub 레포지토리 활용 가이드북</title>
  <style>
    {guidebookCss}
    {pygmentsCss}
  </style>
</head>
<body>
  {htmlBody}
</body>
</html>"""

  return html


def convertHtmlToPdf(html: str, outputPath: Path):
  """HTML을 WeasyPrint로 PDF 변환합니다."""
  try:
    from weasyprint import HTML
    HTML(string=html).write_pdf(str(outputPath))
    print(f"  [완료] PDF 생성: {outputPath}")
  except ImportError:
    print("  [오류] weasyprint가 설치되어 있지 않습니다.")
    print("  pip install weasyprint 를 실행해주세요.")
    print("  (WeasyPrint는 GTK 라이브러리가 필요합니다)")
    print("  Windows: https://doc.courtbouillon.org/weasyprint/stable/first_steps.html")
    return
  except Exception as e:
    print(f"  [오류] PDF 생성 실패: {e}")
    print("  HTML 파일로 대신 저장합니다...")
    # HTML 파일로 대체 저장
    htmlPath = outputPath.with_suffix(".html")
    htmlPath.write_text(html, encoding="utf-8")
    print(f"  [대체] HTML 저장: {htmlPath}")


def main():
  """메인 실행 함수"""
  scriptDir = Path(__file__).parent
  projectRoot = scriptDir.parent
  mdPath = projectRoot / "output" / "Guidebook.md"
  pdfPath = projectRoot / "output" / "Guidebook.pdf"
  cssPath = scriptDir / "guidebook.css"

  print("=" * 60)
  print("  MD → PDF 변환 시작")
  print("=" * 60)

  if not mdPath.exists():
    print(f"[오류] 통합 MD 파일이 없습니다: {mdPath}")
    print("  먼저 md_merger.py를 실행해주세요.")
    return

  mdContent = mdPath.read_text(encoding="utf-8")
  print(f"  [읽기] {mdPath} ({len(mdContent):,} bytes)")

  # HTML 생성
  html = generateHtml(mdContent, cssPath)
  print(f"  [변환] HTML 생성 완료 ({len(html):,} bytes)")

  # PDF 변환
  convertHtmlToPdf(html, pdfPath)


if __name__ == "__main__":
  main()
