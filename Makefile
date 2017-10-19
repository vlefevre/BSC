TEX=pdflatex
BIB=bibtex

STEM=report
DIR=report
INC= $(wildcard report/*.tex)

TARGET=$(STEM).pdf
SRC = $(STEM).tex
AUX = $(STEM).aux

$(TARGET):	$(DIR)/$(SRC) $(INC)
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
