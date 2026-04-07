"""
공통 스타일 설정 모듈
가이드북의 폰트, 색상, 여백 등 공통 스타일을 정의합니다.
"""

from dataclasses import dataclass

# 페이지 설정 (A4)
PAGE_WIDTH_CM = 21.0
PAGE_HEIGHT_CM = 29.7
MARGIN_TOP_CM = 2.54
MARGIN_BOTTOM_CM = 2.54
MARGIN_LEFT_CM = 2.54
MARGIN_RIGHT_CM = 2.54

# 폰트 설정 (한국어 지원)
FONT_BODY = "맑은 고딕"
FONT_BODY_FALLBACK = "Malgun Gothic"
FONT_CODE = "D2Coding"
FONT_CODE_FALLBACK = "Consolas"

# 폰트 크기 (pt)
FONT_SIZE_BODY = 10
FONT_SIZE_H1 = 24
FONT_SIZE_H2 = 18
FONT_SIZE_H3 = 14
FONT_SIZE_H4 = 12
FONT_SIZE_CODE = 9
FONT_SIZE_FOOTER = 8

# 색상 (HEX)
COLOR_PRIMARY = "#1a1a2e"    # 제목 - 짙은 남색
COLOR_SECONDARY = "#16213e"  # 부제목
COLOR_ACCENT = "#0f3460"     # 강조
COLOR_LINK = "#e94560"       # 링크
COLOR_CODE_BG = "#f5f5f5"    # 코드 배경
COLOR_CODE_BORDER = "#e0e0e0"  # 코드 테두리
COLOR_TABLE_HEADER = "#1a1a2e"  # 테이블 헤더 배경
COLOR_TABLE_HEADER_TEXT = "#ffffff"  # 테이블 헤더 텍스트
COLOR_TABLE_ROW_ALT = "#f8f9fa"  # 테이블 짝수행

# 줄 간격
LINE_SPACING = 1.5
CODE_LINE_SPACING = 1.2

# DOCX 스타일명
DOCX_STYLES = {
  "title": "Guidebook Title",
  "heading1": "Guidebook Heading 1",
  "heading2": "Guidebook Heading 2",
  "heading3": "Guidebook Heading 3",
  "heading4": "Guidebook Heading 4",
  "body": "Guidebook Body",
  "code": "Guidebook Code",
  "blockquote": "Guidebook Quote",
  "table_header": "Guidebook Table Header",
}

# src 파일 순서
SRC_FILES = [
  "00_introduction.md",
  "01_foundation.md",
  "02_frameworks.md",
  "03_projects.md",
  "04_document_libraries.md",
  "05_ai_tools.md",
  "06_career.md",
  "appendix.md",
]


@dataclass
class HeadingInfo:
  """목차에 사용할 헤딩 정보"""
  level: int
  text: str
  anchor: str
