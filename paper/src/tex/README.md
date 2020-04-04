# tex

This directory contains the LaTeX template `template.tex` with the `$body$`
sentinel somewhere in it. Use this file to include packages, setup
dimensions, formatting, document style, etc. in raw LaTeX.

The very least this document should contain is:

```tex
\begin{document}
$body$
\end{document}
```

Pandoc, the Markdown compiler, replaces `$body$` with the Markdown and
LaTeX contents of the [../md](../md) folder.
