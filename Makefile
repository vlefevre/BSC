TEX=pdflatex 
BIB=bibtex

STEM=report

TARGET=$(STEM).pdf
SRC = $(STEM).tex
AUX = $(STEM).aux

TARGET:
	$(TEX) $(SRC)
	$(BIB) $(AUX)
	$(TEX) $(SRC)
	$(TEX) $(SRC)


.PHONY: clean
clean:
	rm -f $(TARGET) $(AUX) *.bbl *.blg *.log *.out
