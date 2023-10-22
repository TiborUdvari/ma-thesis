# Notes

How to output incopy file from latex
```
pandoc -s -f latex -t icml -o main.icml main.tex
```

Check the character count
```
pdftotext main.pdf - | iconv -c -t ASCII//TRANSLIT |tr -d " " | wc -m
``` 