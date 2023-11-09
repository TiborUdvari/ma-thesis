# Notes

How to output incopy file from latex
```
pandoc -s -f latex -t icml -o main.icml main.tex
```

Check the character count
```
pdftotext main.pdf - | iconv -c -t ASCII//TRANSLIT |tr -d " " | wc -m
``` 

Generate impositions and crop marks. Note: this is not advanced enough, should just use Adobe tools
```
pdfjam --paper '450mm,320mm' --suffix nup --landscape --frame true --nup 2x2 --outfile output.pdf main.pdf
```