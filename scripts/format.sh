#!/usr/bin/env bash
# 가이드북 원고 자동 포맷팅 + 린팅 스크립트
# 사용법: bash scripts/format.sh
set -e

echo "=== Prettier로 docs/ 마크다운 포맷팅 ==="
prettier --write "docs/**/*.md"

echo ""
echo "=== markdownlint로 docs/ 검수 ==="
markdownlint docs/ || {
  echo ""
  echo "[!] markdownlint 경고가 있습니다. .markdownlint.json 규칙 확인 후 수동 수정하세요."
}

echo ""
echo "=== mkdocs strict 빌드 검증 ==="
PYTHONIOENCODING=utf-8 mkdocs build --strict --clean

echo ""
echo "[완료] 포맷팅 + 린팅 + 빌드 검증 모두 통과"
