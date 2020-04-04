# the default when running `make` in this directory
default: pdf

#
# MARK: build
#

# the build directory
BUILD=build

# a command for making a build directory
build:
	mkdir -p ${BUILD}

#
# MARK: Installation Scripts
#

# install for a Linux machine using `apt-get`
linux_install:
	sudo apt-get -qq update
	sudo apt-get install -y --no-install-recommends texlive-full pandoc pandoc-citeproc

# install for a MacOS machine using `brew`
macos_install:
	brew update
	brew cask install mactex
	brew install pandoc
	brew install pandoc-citeproc

# the system this script is executing on
SYSTEM := $(shell uname -s)
# install the dependencies with OS ambiguity
install:
	@echo 'installing for: $(SYSTEM)'
ifeq "$(SYSTEM)" "Darwin"
	make macos_install
endif
ifeq "$(SYSTEM)" "Linux"
	make linux_install
endif

#
# MARK: find TODO
#

# find the TODO files in each literature directory
find_todo_lit:
	@find 'lit' -type f -name 'TODO'

# find the TODO files in literature notes.md files
find_todo_lit_notes:
	@grep -rnw 'lit' -e 'TODO' || exit 0

# find any TODO statements in the markdown source (or with exit 0)
find_todo_md:
	@grep -rnw 'src/md' -e 'TODO' || exit 0

# find any TODO statements in the python code files (or with exit 0)
find_todo_python:
	@grep -rnw 'src/python' -e 'TODO' || exit 0

#
# MARK: Compilation
#

# the name of the terminal node file to use with find
REFERENCE=reference.bib
# the pattern for comment lines and blank lines to ignore. Note that $ are
# operators in Make and thus are escaped. i.e. $$ means $ at the command line.
COMMENT_REGEX="(%|^$$|^\s*$$)"
# the name of the master file to build
REFERENCES=${BUILD}/references.bib
# Make a global references.bib file from the many reference.bib files
references: build
	cat `find lit -name ${REFERENCE}` | egrep -v ${COMMENT_REGEX} > ${REFERENCES}

# Make a Markdown build file (build.md)
markdown:
	python3 src/python/compile.py

# Compile a document using pandoc
# Args:
# 	1: the output file type (i.e. 'tex' or 'pdf')
define pandoc_compile
	pandoc ${BUILD}/${BUILD}.md \
		-o ${BUILD}/${BUILD}.$(1) \
		--template=${BUILD}/template.tex
endef

# Make a LaTeX build file (build.tex) from the Markdown build file (build.md)
tex: markdown
	$(call pandoc_compile,tex)
	rm -f ${BUILD}/${BUILD}.md
	rm -f ${BUILD}/template.tex

# File-types to clean out from the build folder after pdf compilation
CLEAN=*.aux *.nav *.log *.out *.snm *.toc *.bbl *.blg *.brf *.swp *.nlo *.spl
# Delete all build-time LaTeX and BibTex files
clean_build: build
	cd ${BUILD} && rm -f ${CLEAN}

# Make a pdf build file (build.pdf) using PdfLaTeX and BibTex on the LaTeX
# build file (build.tex)make
pdf: clean_build tex references
	cd ${BUILD} && pdflatex -halt-on-error ${BUILD} | grep -a3 "^!" || true
	cd ${BUILD} && bibtex ${BUILD}
	cd ${BUILD} && pdflatex -halt-on-error ${BUILD} | grep -a3 "^!" || true
	cd ${BUILD} && pdflatex -halt-on-error ${BUILD} | grep -a3 "^!" || true
	@make clean_build

#
# MARK: Word Counts
#

# count the words in the paper (custom Markdown LaTeX parser)
count_words:
	@python3 src/python/count_words.py src/md

# Count the words in the paper (pdf).
count_words_pdf:
	@make pdf > /tmp/null
	@ps2ascii ${BUILD}/${BUILD}.pdf | wc -w
	@echo 'words in ${BUILD}/${BUILD}.pdf'
