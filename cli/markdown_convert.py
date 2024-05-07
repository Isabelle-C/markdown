#!/usr/bin/env python3

import click
from src.markdown.markdown import MarkDown


@click.command()
@click.argument("input_path")
@click.argument("output_path")
def convert(input_path, output_path):
    """
    Convert a Markdown file to another document format.
    """
    pdf = MarkDown(input_path)

    if output_path.endswith(".docx"):
        pdf.to_word(output_path)
    elif output_path.endswith(".pdf"):
        pdf.to_pdf(output_path)
    else:
        print("Invalid output format.")

if __name__ == "__main__":
    convert()
