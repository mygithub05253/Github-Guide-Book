"""
MD 파일 병합 + 목차 생성 스크립트
src/ 디렉토리의 마크다운 파일들을 순서대로 병합하고 목차를 자동 생성합니다.
"""

import re
import os
from pathlib import Path
from style_config import SRC_FILES, HeadingInfo


def extractHeadings(content: str) -> list[HeadingInfo]:
  """마크다운 내용에서 헤딩(## 이상)을 추출합니다.

  코드 블록 파싱 규칙:
  - 코드 블록 밖: ```lang 또는 ``` 으로 시작하면 코드 블록 진입
  - 코드 블록 안: 닫는 펜스는 공백/탭만 허용된 단독 ``` 줄만 인식
    (언어 태그가 붙은 ```bash 같은 줄은 코드 블록 내부 텍스트로 간주)
  """
  headings = []
  inCodeBlock = False

  for line in content.split("\n"):
    if inCodeBlock:
      # 닫는 펜스는 정확히 ``` (앞뒤 공백만 허용)
      if re.match(r"^\s*```\s*$", line):
        inCodeBlock = False
      continue

    # 코드 블록 밖: ``` 또는 ```언어 로 시작하면 진입
    if line.lstrip().startswith("```"):
      inCodeBlock = True
      continue

    match = re.match(r"^(#{1,4})\s+(.+)$", line)
    if match:
      level = len(match.group(1))
      text = match.group(2).strip()
      # 앵커 생성 (GitHub 스타일)
      anchor = re.sub(r"[^\w\s가-힣-]", "", text.lower())
      anchor = re.sub(r"\s+", "-", anchor.strip())
      headings.append(HeadingInfo(level=level, text=text, anchor=anchor))

  return headings


def generateToc(headings: list[HeadingInfo]) -> str:
  """헤딩 목록으로 마크다운 목차를 생성합니다."""
  tocLines = ["# 목차\n"]

  for h in headings:
    if h.level > 3:
      continue  # H4 이하는 목차에서 제외

    indent = "  " * (h.level - 1)
    tocLines.append(f"{indent}- [{h.text}](#{h.anchor})")

  tocLines.append("\n---\n")
  return "\n".join(tocLines)


def mergeMdFiles(srcDir: Path, outputPath: Path) -> str:
  """src/ 디렉토리의 MD 파일들을 병합합니다."""
  mergedContent = []

  for filename in SRC_FILES:
    filePath = srcDir / filename
    if not filePath.exists():
      print(f"  [경고] {filename} 파일이 없습니다. 건너뜁니다.")
      continue

    content = filePath.read_text(encoding="utf-8")
    mergedContent.append(content)
    # 파트 사이에 구분선 추가
    mergedContent.append("\n\n---\n\n")
    print(f"  [병합] {filename} ({len(content):,} bytes)")

  fullContent = "\n".join(mergedContent)

  # 목차 생성
  headings = extractHeadings(fullContent)
  toc = generateToc(headings)

  # 첫 번째 파트(소개) 뒤에 목차 삽입
  # 소개 파트의 첫 번째 --- 이후에 삽입
  parts = fullContent.split("\n---\n", 1)
  if len(parts) == 2:
    finalContent = parts[0] + "\n---\n\n" + toc + "\n" + parts[1]
  else:
    finalContent = toc + "\n" + fullContent

  # 파일 저장
  outputPath.parent.mkdir(parents=True, exist_ok=True)
  outputPath.write_text(finalContent, encoding="utf-8")

  lineCount = finalContent.count("\n") + 1
  print(f"\n  [완료] 통합 파일 생성: {outputPath}")
  print(f"  [정보] 총 {lineCount:,} 줄, {len(finalContent):,} bytes")
  print(f"  [정보] 목차 항목: {len(headings)}개")

  return finalContent


def main():
  """메인 실행 함수"""
  # 프로젝트 루트 경로
  scriptDir = Path(__file__).parent
  projectRoot = scriptDir.parent
  srcDir = projectRoot / "src"
  outputPath = projectRoot / "output" / "Guidebook.md"

  print("=" * 60)
  print("  MD 파일 병합 시작")
  print("=" * 60)

  if not srcDir.exists():
    print(f"[오류] src 디렉토리가 없습니다: {srcDir}")
    return None

  content = mergeMdFiles(srcDir, outputPath)
  return content


if __name__ == "__main__":
  main()
