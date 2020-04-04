# the build folder within this directory
BUILD=build
# the filetype of the output images (this is a PlantUML flag)
OUTPUT_FILETYPE=-tsvg

# make everything in this script
all: clean pdf

#
# MARK: Installation Scripts
#

# install for a Linux machine using `apt-get`
linux_install:
	sudo apt-get -qq update
	sudo apt-get install -y plantuml

# install for a MacOS machine using `brew`
macos_install:
	brew update
	brew install plantuml

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
# MARK: Build
#

# remove any files created by make
clean:
	rm -rf build

# make a build folder for build artifacts
build:
	mkdir -p ${BUILD}

# make the UML diagrams
uml: build *.puml
	plantuml -nbthread auto -o ${BUILD} ${OUTPUT_FILETYPE} *.puml

# convert the SVG output to PDF (internal PDF mechanism with PlantUML is bad)
pdf: uml
	@for filename in ${BUILD}/*.svg; do \
		rsvg-convert -f pdf -o $${filename%%.*}.pdf $$filename; \
	done
