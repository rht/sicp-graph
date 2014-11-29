mkdir -p markdown
find html/ -name \*.html -type f -exec pandoc -o {}.md {} \;
mv html/*.md markdown
