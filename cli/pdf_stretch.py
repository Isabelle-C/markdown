#!/usr/bin/env python3

import click
from src.pdf.pdf import Pdf


@click.command()
@click.argument("input_pdf_path")
@click.argument("output_pdf_path")
@click.option("--extra_margin", "-m", default=250, help="Extra margin to add to the right of each page.")
def add_right_margin(input_pdf_path, output_pdf_path, extra_margin=250):
    """
    Adds a right margin to each page of a PDF.
    
    Parameters:
    - input_pdf_path: Path to the input PDF file.
    - output_pdf_path: Path where the output PDF with the right margin will be saved.
    """
    pdf = Pdf(input_pdf_path)
    pdf.add_right_margin(output_pdf_path, extra_margin)

if __name__ == "__main__":
    add_right_margin()
