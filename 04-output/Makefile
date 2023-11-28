.PHONY: print
dev:
	latexmk -xelatex -shell-escape -synctex=1 -interaction=errorstopmode -file-line-error -output-directory=./out -pvc -f main.tex

build:
	latexmk -xelatex -shell-escape -synctex=1 -interaction=errorstopmode -file-line-error -output-directory=./out -f main.tex

clean:
	rm ./out/*.aux ./out/*.log ./out/*.toc ./out/*.lof ./out/*.lot ./out/*.out ./out/*.synctex.gz ./out/*.synctex ./out/*.fls ./out/*.fdb_latexmk

print:
	echo "Generating print files" && python3 extract_pages.py ./out/main intropage largepage -d print

cc:
	pdftotext out/main.pdf - | iconv -c -t ASCII//TRANSLIT |tr -d " " | wc -m

ssmall:
	pdfinfo print/main_untagged_pages.pdf | grep "Page size" | grep -Eo '[-+]?[0-9]*\.?[0-9]+' | awk -v x=0.3528 '{print $$1*x}'

slarge:
	pdfinfo print/main_largepage_extracted.pdf | grep "Page size" | grep -Eo '[-+]?[0-9]*\.?[0-9]+' | awk -v x=0.3528 '{print $$1*x}'

sintro:
	pdfinfo print/main_intropage_extracted.pdf | grep "Page size" | grep -Eo '[-+]?[0-9]*\.?[0-9]+' | awk -v x=0.3528 '{print $$1*x}'

sizes:
	$(MAKE) ssmall
	$(MAKE) slarge
	$(MAKE) sintro