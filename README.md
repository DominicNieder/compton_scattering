# Compton Experiment

### Preliminaries: Github settings
- fist add a file named ".gitignore" this will automatically be recognised by Git, so that it ignores all files (pdf for reading, *.log, etc...) that are not required to be shared.
Here my the content of my .gitignore file: 
> # my literature to read (comments in .gitingore)
> reading/
> 
> # any other pdf, also from .tex
> *.pdf
> 
> # latex specific
> *.out
> *.fls
> *.log
> *.xml
> *.sta
> *.gz
> *.aux
> *.bbl
> *.fdb_latexmk
> *.bcf
> *.blg
> *.toc
> 
> # do not change
> .gitignore
> 
> # my python environment
> analysis-code/.compton_environment/


### Report and Latex

Depending on from which directory the "main.tex" will be compiled from, the **figures/picutres will be accessed by a different path**. 

In report/main.tex there is a line that fill access all figures from figure/ and, or pictures/

run from commandline:
> cd report && pdflatex main.tex