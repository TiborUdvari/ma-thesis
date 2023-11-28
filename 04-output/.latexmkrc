# 1. Biber active
# $biber="echo 'skipping biber'"

# 2. Biber inactive
# Use Biber as bibtex backend
$biber = 'biber %O %B';
$bib_program = 'biber';

# Use this for pdflatex
#$pdf_mode = 1;

# Use this for lualatex
#$pdf_mode = 4;

# Use this for xelatex
$pdf_mode = 5;

# Recompile if .bib files change
$watch_files = [ 'bib' ];