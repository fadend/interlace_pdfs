"""Interlace PDF files into a single PDF.

This is a very thin wrapper around the PyPDF2 library.

It was inspired by https://automatetheboringstuff.com/2e/chapter15/."""

import argparse
import itertools

import PyPDF2


def main():
    parser = argparse.ArgumentParser(
        prog="merge_pdfs", description="Merge PDFs into a single PDF file"
    )
    parser.add_argument("-o", "--output", required=True)
    parser.add_argument("input_files", nargs=2)
    args = parser.parse_args()
    writer = PyPDF2.PdfWriter()
    file1, file2 = args.input_files
    reader1 = PyPDF2.PdfReader(file1)
    reader2 = PyPDF2.PdfReader(file2)
    for page1, page2 in itertools.zip_longest(reader1.pages, reader2.pages):
        if page1:
            writer.add_page(page1)
        if page2:
            writer.add_page(page2)
    writer.write(args.output)


if __name__ == "__main__":
    main()
