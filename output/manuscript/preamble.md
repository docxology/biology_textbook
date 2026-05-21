<!--
  preamble.md — LaTeX preamble for Biology Textbook PDF output.
  Parsed by infrastructure/rendering/pdf_renderer.py.
  All content inside ```latex ... ``` fences is injected before \begin{document}.

  Layout values mirror manuscript/config.yaml (keep in sync when editing).
-->

```latex
% -----------------------------------------------------------------------
% PAGE GEOMETRY  (config.yaml: layout.*)
% Near-zero margins: 2 mm all sides (matches config.yaml layout.margin_*_mm).
% -----------------------------------------------------------------------
\usepackage[
  top=2mm,
  bottom=2mm,
  left=2mm,
  right=2mm,
  headheight=12pt,
  includeheadfoot
]{geometry}

% -----------------------------------------------------------------------
% HYPERLINK COLOURS — red links regardless of pandoc hidelinks.
%
% Strategy: PassOptionsToPackage fires BEFORE hyperref is loaded by Pandoc,
% so colorlinks=true wins over hidelinks.  AtBeginDocument then re-applies
% the complete hypersetup as a belt-and-braces override.
% -----------------------------------------------------------------------
\PassOptionsToPackage{colorlinks=true,urlcolor=red,linkcolor=red,citecolor=red}{hyperref}

\AtBeginDocument{%
  \hypersetup{colorlinks=true,urlcolor=red,linkcolor=red,citecolor=red,
              anchorcolor=red,filecolor=red,menucolor=red}%
}

% -----------------------------------------------------------------------
% TYPOGRAPHY  (config.yaml: typography.*)
% Body: Linux Libertine O or STIX Two Text | Heading: Linux Biolinum O or Arial
% -----------------------------------------------------------------------
\usepackage{fontspec}
\IfFontExistsTF{Linux Libertine O}{\setmainfont{Linux Libertine O}}{%
  \IfFontExistsTF{STIX Two Text}{\setmainfont{STIX Two Text}}{}%
}
\IfFontExistsTF{Linux Biolinum O}{\setsansfont{Linux Biolinum O}}{%
  \IfFontExistsTF{Arial}{\setsansfont{Arial}}{}%
}
\IfFontExistsTF{DejaVu Sans Mono}{\setmonofont[Scale=0.88]{DejaVu Sans Mono}}{%
  \IfFontExistsTF{Menlo}{\setmonofont[Scale=0.82]{Menlo}}{}%
}
\usepackage{microtype} % Enhances typographic quality (kerning, tracking)
\emergencystretch=8em
\sloppy
\raggedbottom

% Text-macro fallbacks for symbols that Pandoc may emit from code or bookmarks.
% Literal Unicode cleanup is handled upstream by the PDF remapper so the preamble
% itself does not introduce missing-glyph warnings.
\newcommand{\TextSafePipe}{\rule[-0.15ex]{0.35pt}{1.2ex}}
\renewcommand{\textasciitilde}{about }
\renewcommand{\textbar}{\TextSafePipe}
\providecommand{\VerbBar}{|}
\renewcommand{\VerbBar}{\TextSafePipe}

% Body size 9/10.8 pt (matches config.yaml typography.base_font_size_pt)
\makeatletter
\renewcommand{\normalsize}{%
  \@setfontsize\normalsize{9}{10.8}%
}
\makeatother
\normalsize

% -----------------------------------------------------------------------
% MATHEMATICS  (equation numbering with \eqref support)
% -----------------------------------------------------------------------
\usepackage{amsmath}
\usepackage{amssymb}
\IfFontExistsTF{STIX Two Math}{\setmathfont{STIX Two Math}}{}

% -----------------------------------------------------------------------
% CROSS-REFERENCES  (cleveref — must load AFTER hyperref+amsmath)
% Enables \cref{sec:foo} / \Cref{fig:bar} to render as "section 3" / "Figure 4.2"
% without hard-coding the kind word. Works with every \label{sec:...},
% \label{fig:...}, \label{eq:...}, \label{tbl:...} in the manuscript.
% -----------------------------------------------------------------------
\usepackage[capitalise,noabbrev]{cleveref}
\crefname{section}{section}{sections}
\Crefname{section}{Section}{Sections}
\crefname{figure}{figure}{figures}
\Crefname{figure}{Figure}{Figures}
\crefname{table}{table}{tables}
\Crefname{table}{Table}{Tables}
\crefname{equation}{equation}{equations}
\Crefname{equation}{Equation}{Equations}

% -----------------------------------------------------------------------
% BIBLIOGRAPHY  (natbib for \citep / \citet author-year citations)
% Pandoc auto-injects \usepackage{natbib} and \bibliographystyle{plainnat}
% when citations are present, so we do NOT re-declare them here to avoid
% "Illegal, another \bibstyle command" from bibtex.
% -----------------------------------------------------------------------

% -----------------------------------------------------------------------
% GRAPHICS  (required for \includegraphics)
% -----------------------------------------------------------------------
\usepackage{graphicx}
\makeatletter
\@ifundefined{pandocbounded}{}{%
  \renewcommand*\pandocbounded[1]{%
    \sbox\pandoc@box{#1}%
    \Gscale@div\@tempa{0.72\textheight}{\dimexpr\ht\pandoc@box+\dp\pandoc@box\relax}%
    \Gscale@div\@tempb{\linewidth}{\wd\pandoc@box}%
    \ifdim\@tempb\p@<\@tempa\p@\let\@tempa\@tempb\fi%
    \ifdim\@tempa\p@<\p@\scalebox{\@tempa}{\usebox\pandoc@box}%
    \else\usebox{\pandoc@box}%
    \fi%
  }%
}
\renewcommand{\topfraction}{0.92}
\renewcommand{\bottomfraction}{0.82}
\renewcommand{\textfraction}{0.06}
\renewcommand{\floatpagefraction}{0.74}
\setcounter{topnumber}{4}
\setcounter{bottomnumber}{3}
\setcounter{totalnumber}{6}
\makeatother

% -----------------------------------------------------------------------
% SECTION HEADER STYLE — compact sans-serif headings
% -----------------------------------------------------------------------
\usepackage{titlesec}
\titleformat{\section}{\normalfont\large\bfseries\sffamily}{\thesection}{0.85em}{}
\titleformat{\subsection}{\normalfont\normalsize\bfseries\sffamily}{\thesubsection}{0.85em}{}
\titleformat{\subsubsection}{\normalfont\small\bfseries\sffamily}{\thesubsubsection}{0.85em}{}
\titlespacing*{\section}{0pt}{10pt plus 2pt minus 2pt}{4pt plus 1pt}
\titlespacing*{\subsection}{0pt}{8pt plus 2pt minus 2pt}{3pt plus 1pt}

% -----------------------------------------------------------------------
% TABLE OF CONTENTS
% -----------------------------------------------------------------------
\usepackage{tocloft}
\setcounter{tocdepth}{3}
\setcounter{secnumdepth}{3}
\setlength{\cftsecnumwidth}{3.6em}
\setlength{\cftsubsecnumwidth}{4.8em}
\setlength{\cftsubsubsecnumwidth}{6.2em}
\renewcommand{\cftsecleader}{\cftdotfill{\cftdotsep}}
\renewcommand{\cftsubsecleader}{\cftdotfill{\cftdotsep}}
\renewcommand{\cftsubsubsecleader}{\cftdotfill{\cftdotsep}}

% -----------------------------------------------------------------------
% FIGURE / TABLE CAPTIONS
% -----------------------------------------------------------------------
\usepackage[font=footnotesize,labelfont=bf,labelsep=period]{caption}

% -----------------------------------------------------------------------
% LINE SPACING  (config.yaml: layout.line_height = 1.28)
% -----------------------------------------------------------------------
\usepackage{setspace}
\setstretch{1.28}

% -----------------------------------------------------------------------
% HEADER / FOOTER
% -----------------------------------------------------------------------
\usepackage{fancyhdr}
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\footnotesize\sffamily\nouppercase{\leftmark}}
\fancyhead[R]{\footnotesize\sffamily Introduction to Biology}
\fancyfoot[C]{\footnotesize\thepage}
\renewcommand{\headrulewidth}{0.4pt}
```
