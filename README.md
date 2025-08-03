# LLNCS LaTeX Template with Biblatex

A modern, organized LaTeX template for Springer's **Lecture Notes in Computer Science (LLNCS)** proceedings, based on the [official Springer guidelines](https://www.springer.com/gp/computer-science/lncs/conference-proceedings-guidelines). This template has been enhanced with **biblatex** (replacing the traditional BibTeX workflow) and features **compact numeric citations** instead of the standard `splncs04` style, along with modular file organization for better project management.

## 📁 Project Structure

```
├── main.tex                 # Main document file
├── bibliography.bib         # Bibliography entries (biblatex format)
├── Body/                    # Content organization
│   ├── abstract.tex         # Abstract and keywords
│   ├── intro.tex           # Introduction section
│   ├── background.tex      # Background section
│   ├── methodology.tex     # Methodology section
│   ├── results.tex         # Results section
│   ├── related.tex         # Related work section
│   └── tables/
│       └── example.tex     # Table definitions
├── output/                 # Compiled PDFs and auxiliary files
├── llncs.cls              # LLNCS document class
├── splncs04.bst           # Legacy BibTeX style (not used)
├── fig1.eps               # Sample figure
└── sync_overleaf.py       # Overleaf synchronization script
```

## 🚀 Quick Start

### Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```

2. **DevContainer Setup** (if using):
   - Adjust the username in `.devcontainer/` configuration files to match your system
   - This prevents permission issues when working in containerized environments
   - The devcontainer provides a consistent LaTeX environment across different systems

3. **Overleaf Integration** (optional):
   - Use `sync_overleaf.py` script to synchronize with Overleaf projects
   - Configure your Overleaf project details in the script
   - Enables seamless collaboration between local development and Overleaf

### Prerequisites

- **LaTeX Distribution**: TeX Live, MiKTeX, or MacTeX
- **Backend**: Biber (for biblatex)
- **Recommended**: VSCode with LaTeX Workshop or TeXShop/TeXworks

### Compilation

The template uses **biblatex** with **biber** backend. Use this compilation sequence:

```bash
pdflatex main.tex
biber main
pdflatex main.tex
pdflatex main.tex
```

Or configure your LaTeX editor to use `biber` instead of `bibtex`.

### Modern LaTeX Editors

Most modern editors handle this automatically:
- **VSCode + LaTeX Workshop**: Set `latex-workshop.latex.tools` to use biber
- **Overleaf**: Automatically detects biblatex
- **TeXShop**: Set engine to "pdflatexmk" or configure custom engine

## ✨ Features

### Enhanced Bibliography Management
- **Biblatex**: Modern, Unicode-aware bibliography system
- **Biber Backend**: Superior sorting and formatting capabilities
- **Numeric-Comp Style**: Compressed citations `[1-3,5]` for space efficiency
- **Flexible Citation Commands**: `\cite{}`, `\textcite{}`, `\parencite{}`, etc.

### Modular Organization
- **Sectioned Content**: Separate files for each major section
- **Table Management**: Organized table definitions in `Body/tables/`
- **Clean Main File**: Focus on structure, not content details

### LLNCS Compliance
- **Official Class**: Uses Springer's `llncs.cls` (v2.21)
- **Proper Formatting**: Headers, footers, and spacing per LLNCS requirements
- **T1 Font Encoding**: Ensures proper character rendering in final PDFs

## 🔄 Key Changes from Official Template

This template is based on the [official Springer LNCS template](https://www.springer.com/gp/computer-science/lncs/conference-proceedings-guidelines) with several modern improvements:

### Bibliography System Upgrade
- **From BibTeX to Biblatex**: Replaced the traditional `splncs04.bst` style with modern biblatex
- **From `splncs04` to `numeric-comp`**: Changed citation style for better space efficiency
- **Enhanced Backend**: Uses Biber instead of BibTeX for superior Unicode and sorting support

### Development Workflow
- **DevContainer Support**: Consistent LaTeX environment across different systems
- **Overleaf Integration**: `sync_overleaf.py` script for seamless cloud collaboration
- **Modular Structure**: Organized content into logical files for better project management

### Compatibility
- **LLNCS Compliant**: Maintains full compatibility with Springer's formatting requirements
- **Modern LaTeX**: Leverages contemporary LaTeX packages and best practices
- **Flexible Citations**: Multiple citation styles available while maintaining LLNCS appearance

## 📝 Usage Guide

### 1. Document Metadata

Edit the frontmatter in `main.tex`:

```latex
\title{Your Paper Title}
\author{Your Name\inst{1}\orcidID{0000-0000-0000-0000}}
\institute{Your Institution\\
\email{your.email@institution.edu}}
```

### 2. Abstract and Keywords

Edit `Body/abstract.tex`:

```latex
\begin{abstract}
    Your abstract here (150-250 words).
    
    \keywords{Keyword 1 \and Keyword 2 \and Keyword 3}
\end{abstract}
```

### 3. Content Sections

Add content to the respective files in `Body/`:
- `intro.tex` - Introduction
- `background.tex` - Background/Related Work
- `methodology.tex` - Your methodology
- `results.tex` - Results and evaluation
- `related.tex` - Related work (if separate from background)

Include sections in `main.tex`:
```latex
\input{Body/intro.tex}
\input{Body/methodology.tex}
\input{Body/results.tex}
```

### 4. Bibliography

Add references to `bibliography.bib`:

```bibtex
@article{your_ref,
  author  = {Author, First and Author, Second},
  title   = {Paper Title},
  journal = {Journal Name},
  volume  = {42},
  pages   = {1--10},
  year    = {2024}
}
```

Cite in text:
```latex
\cite{your_ref}                    % [1]
\textcite{your_ref}               % Author et al. [1]
\parencite{your_ref}              % (Author et al., 2024)
\cite{ref1,ref2,ref3}             % [1-3] (compressed)
```

### 5. Tables and Figures

Store table definitions in `Body/tables/` and include them:

```latex
\input{Body/tables/results_table.tex}
```

For figures:
```latex
\begin{figure}
    \includegraphics[width=\textwidth]{your_figure.pdf}
    \caption{Your caption here.}
    \label{fig:your_label}
\end{figure}
```

## ⚙️ Configuration Options

### Bibliography Styles

Change the style in `main.tex`:

```latex
% Current: Compressed numeric citations [1-3,5]
\usepackage[backend=biber, style=numeric-comp, sorting=none]{biblatex}

% Alternatives:
% style=ieee          % IEEE style [1], [2], [3]
% style=alphabetic    % Author-year abbreviations [ABC+24]
% style=authoryear    % Full author-year (Author et al., 2024)
```

### Sorting Options

```latex
sorting=none     % Order of first citation (recommended)
sorting=nty      % Name, title, year
sorting=ynt      % Year, name, title
```

### Optional Packages

Uncomment in `main.tex` for additional features:

```latex
% For colored URLs
\usepackage{color}
\renewcommand\UrlFont{\color{blue}\rmfamily}

% For hyperlinks
\usepackage{hyperref}
```

## 🔧 Troubleshooting

### Common Issues

**Bibliography not appearing**:
- Ensure you run `biber main` (not `bibtex main`)
- Check for syntax errors in `bibliography.bib`
- Verify `\addbibresource{bibliography.bib}` path

**Citations showing as [?]**:
- Complete the full compilation sequence
- Check citation keys match entries in `.bib` file

**LaTeX errors with special characters**:
- Use T1 font encoding (already included)
- Ensure UTF-8 file encoding
- Escape special characters: `\&`, `\%`, `\$`, etc.

**LLNCS formatting issues**:
- Don't modify `llncs.cls`
- Follow LLNCS guidelines for section structure
- Use provided environments: `theorem`, `proof`, `definition`

### Editor Configuration

**VSCode** (`settings.json`):
```json
{
    "latex-workshop.latex.tools": [
        {
            "name": "pdflatex",
            "command": "pdflatex",
            "args": ["-synctex=1", "-interaction=nonstopmode", "%DOC%"]
        },
        {
            "name": "biber",
            "command": "biber",
            "args": ["%DOCFILE%"]
        }
    ],
    "latex-workshop.latex.recipes": [
        {
            "name": "pdflatex → biber → pdflatex×2",
            "tools": ["pdflatex", "biber", "pdflatex", "pdflatex"]
        }
    ]
}
```

## 📚 Resources

### LLNCS Guidelines
- [**Official Springer LNCS Guidelines**](https://www.springer.com/gp/computer-science/lncs/conference-proceedings-guidelines) - Primary source for this template
- [LNCS Author Instructions (PDF)](https://www.springer.com/gp/computer-science/lncs/conference-proceedings-guidelines) - Detailed formatting requirements
- [Official LaTeX Templates](https://www.springer.com/gp/computer-science/lncs/conference-proceedings-guidelines) - Original BibTeX-based templates

### Biblatex Documentation
- [Biblatex Manual](https://ctan.org/pkg/biblatex)
- [Biber Manual](https://ctan.org/pkg/biber)
- [Citation Styles Gallery](https://www.overleaf.com/learn/latex/Biblatex_citation_styles)

### LaTeX Resources
- [CTAN](https://www.ctan.org/) - Comprehensive TeX Archive Network
- [LaTeX Wikibook](https://en.wikibooks.org/wiki/LaTeX)
- [Overleaf Documentation](https://www.overleaf.com/learn)

## 📄 License

This template includes:
- **LLNCS class files**: © Springer-Verlag (use per conference guidelines)
- **Template organization**: Free to use and modify
- **Sample content**: Replace with your own research

## 🤝 Contributing

Feel free to improve this template:
1. Fork the repository
2. Create a feature branch
3. Submit a pull request

---

**Happy LaTeX writing!** 🎓

For questions about LLNCS formatting, consult the official Springer guidelines. For biblatex issues, check the comprehensive documentation or community forums.
