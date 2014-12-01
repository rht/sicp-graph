mkdir -p sicm/markdown
find sicm/html/ -name \*.html -type f -exec pandoc -o {}.md {} \;
mv sicm/html/*.md sicm/markdown
