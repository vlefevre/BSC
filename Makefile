TEX=pdflatex 
BIB=bibtex

STEM=report
DIR=report

TARGET=$(STEM).pdf
SRC = $(STEM).tex
AUX = $(STEM).aux

TARGET:
	cd $(DIR); \
	$(TEX) $(SRC);\
	$(BIB) $(AUX); \
	$(TEX) $(SRC);\
	$(TEX) $(SRC)


.PHONY: clean
clean:
	rm -f $(DIR)/$(TARGET) $(DIR)/$(AUX) $(DIR)/*.bbl $(DIR)/*.blg $(DIR)/*.log $(DIR)/*.out
