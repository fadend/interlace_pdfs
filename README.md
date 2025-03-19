# Interlace PDF files into a single PDF

Takes two PDF files and interlaces the pages, taking the first page from the first,
then the first page from the second, and so on.

This can be helpful, e.g., if your scanner document feeder handles only
one-sided documents giving you intermediate PDFs with the odd and even pages.

## Usage

```
python -m venv interlaceenv
cd interlaceenv
bin/pip3 install git+https://github.com/fadend/interlace_pdfs
bin/python -m interlace_pdfs.interlace_pdfs -o $HOME/doc.pdf $HOME/doc/pages1_3_5.pdf $HOME/doc/pages2_4_6.pdf
```

## Acknowledgments

This is a thin wrapper around the [PyPDF2](https://pypi.org/project/PyPDF2/) package,
which I learned about from
[Automate the Boring Stuff with Python, Chapter 15](https://automatetheboringstuff.com/2e/chapter15/).

Formatted using [black](https://github.com/psf/black).
