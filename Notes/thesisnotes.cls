\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{thesisnotes}[2025/04/09 Thesis-Style Note-Taking Template]

\LoadClass[12pt]{article}

% Required Packages
\RequirePackage[utf8]{inputenc}
\RequirePackage[english]{babel}
\RequirePackage[a4paper, margin=1in, headheight=14.5pt]{geometry}
\RequirePackage{setspace}
\RequirePackage{lmodern}
\RequirePackage{xcolor}
\RequirePackage{fancyhdr}
\RequirePackage{datetime}
\RequirePackage{titlesec}
\RequirePackage{marginnote}
\RequirePackage{enumitem}
\RequirePackage{tcolorbox}
\RequirePackage{amsmath}
\RequirePackage{amssymb}
\RequirePackage[parfill]{parskip}
\RequirePackage{listings}
\RequirePackage{hyperref}
\def\DefaultHeightofCheckBox{0.6\baselineskip}
\def\DefaultWidthofCheckBox{0.6\baselineskip}

\RequirePackage{tikz}
% Line spacing
\onehalfspacing

% Header/Footer
\pagestyle{fancy}
\fancyhf{}
\rhead{\today}
\lhead{Notes}
\rfoot{\thepage}
\lfoot{\textit{Summary by Priyankar}}

% Section formatting
\titleformat{\section}{\Large\bfseries}{\thesection}{1em}{}
\titleformat{\subsection}{\large\bfseries}{\thesubsection}{1em}{}

% Margin notes reversed
\reversemarginpar

% Title box setup
\tcbset{
  mytitlebox/.style={
    colback=gray!10,
    colframe=black,
    fonttitle=\bfseries,
    sharp corners,
    boxrule=0.5pt,
    width=\textwidth,
  }
}
