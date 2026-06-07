#!/bin/bash
# 编译一个 .tex (XeLaTeX)，输出简洁的 PASS/FAIL 与关键错误。
# 用法: bash compile_tex.sh <path/to/file.tex>
export PATH="$HOME/Library/TinyTeX/bin/universal-darwin:$PATH"
TEX="$1"
DIR="$(cd "$(dirname "$TEX")" && pwd)"
BASE="$(basename "$TEX" .tex)"
cd "$DIR" || exit 2
latexmk -xelatex -interaction=nonstopmode -halt-on-error -file-line-error "$BASE.tex" > build.log 2>&1
RC=$?
if [ -f "$BASE.pdf" ] && [ $RC -eq 0 ]; then
  PAGES=$(/Users/yye/project/python/bin/python3 -c "import fitz;print(fitz.open('$DIR/$BASE.pdf').page_count)" 2>/dev/null)
  echo "PASS: $DIR/$BASE.pdf (pages=$PAGES)"
else
  echo "FAIL (rc=$RC). 关键错误如下:"
  grep -E ":[0-9]+:|^!|Undefined|Missing|Runaway|Emergency|not found|Fatal" build.log | head -30
  echo "--- build.log 尾部 ---"
  tail -20 build.log
fi
