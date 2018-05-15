TEX=pdflatex
BIB=bibtex

STEM=report
DIR=cluster2018
INC= $(wildcard $(DIR)/*.tex)

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
