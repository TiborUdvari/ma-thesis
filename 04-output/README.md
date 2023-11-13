# Notes

## Print settings with indesing
* Install multi page importer for indesign
https://github.com/mike-edel/ID-MultiPageImporter/releases
* Save As the resulting PDF with acrobat
* Make new indesign document with correct size, ex `158mm:210mm`
* `Window -> Scripts -> User -> MultiPageImporter` Place the file saved with Acrobat
* In indesing print a booklet if there is enough space on the paper. 2 up perfect bound, 100% scale, flip on short edge, Marks and Bleeds - Crop marks

Extract pages with custom tags for printing
```
python extract_pages.py base_filename tag1 tag2
python extract_pages.py ./out/main-koma mytag -d print
```

Compile document
```
xelatex -shell-escape -synctex=1 -interaction=nonstopmode -file-line-error -output-directory=./out main.tex
```

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