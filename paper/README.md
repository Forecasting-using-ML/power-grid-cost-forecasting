# Paper Repository

## Getting Started

These instructions will get you a copy of the project up and running on your
local machine.

### Prerequisites

This project uses [python3][python] and the Gnu tool [Make][].

#### MacOS

MacOS users will need to install [Homebrew][brew] to install dependencies.

### Installation

Install dependencies for a Linux or MacOS based system:

```shell
make install
```

## Usage

The paper is divided into functional components by file-type, much like most
HTML projects:

| Directory      | Description
|:---------------|:---------------------------------------------------------|
| [src/md][]     | Markdown (.md, .markdown) and LaTeX (.tex) files
| [src/md/img][] | figures, images, and illustrations (.pdf, .png)
| [src/python][] | Python3 scripts for automated tasks (.py)
| [src/tex][]    | The core LaTeX template (template.tex)
| [lit][]        | Literature (.pdf, .txt) BibTex reference files (.bib)

Each directory contains a `README.md` with a description of its usage and
contents.

### References

Recursively find and concatenate each `reference.bib` file in [lit][]
into a build file [build/references.bib][]:

```shell
make references
```

### Paper Compilation

#### Markdown

Concatenate all the LaTeX (.tex) and Markdown (.markdown, .md) files in
[src/md][] in _alphanumeric_ order into a single file [build/build.md][]:

```shell
make markdown
```

#### LaTeX

Generate a file, [build/build.tex][], using [pandoc][], the Markdown build
file ([build/build.md][]) and the LaTeX template ([src/tex/template.tex][]):

```shell
make tex
```

#### PDF

Convert the LaTeX build file ([build/build.tex][]) and built references file
([build/references.bib][]) into a pdf build file [build/build.pdf][] using
[pdflatex][] and [bibtex][]:

```shell
make pdf
```

### Word Count

#### Markdown

Iterate over the LaTeX and Markdown files in [src/md][] and count all of the
words in the _prose only_:

```shell
make count_words
```

**NOTE** No captions, tables, or other text inside of LaTeX commands will be
counted. Comments are also ignored.

#### PDF

Build a `.pdf` and count the words in it:

```shell
make count_words_pdf
```


<!-- Source files -->
[lit]: ./lit
[src/md]: ./src/md
[src/md/img]: ./src/md/img
[src/tex]: ./src/tex
[src/python]: ./src/python
[src/tex/template.tex]: src/tex/template.tex
<!-- Build Files -->
[build/build.md]: build/build.md
[build/build.tex]: build/build.tex
[build/build.pdf]: build/build.pdf
[build/references.bib]: build/references.bib
<!-- Tools -->
[Make]: https://www.gnu.org/software/make/
[brew]: https://brew.sh
[python]: https://www.python.org
[pandoc]: https://pandoc.org
[pdflatex]: https://www.tug.org/applications/pdftex/
[bibtex]: http://www.bibtex.org/
