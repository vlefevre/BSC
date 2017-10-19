TEX=pdflatex
BIB=bibtex

STEM=report
DIR=report

TARGET=$(STEM).pdf
SRC = $(STEM).tex
AUX = $(STEM).aux

$(TARGET):	$(DIR)/$(SRC)
		cd $(DIR); \
		$(TEX) $(SRC);\
		$(BIB) $(AUX); \
		$(TEX) $(SRC);\
		$(TEX) $(SRC); \
        	mv $(TARGET) ..

view:		$(TARGET)
		evince $(TARGET)

.PHONY: clean
clean:
	rm -f $(TARGET) $(DIR)/$(AUX) $(DIR)/*.bbl $(DIR)/*.blg $(DIR)/*.log $(DIR)/*.out
