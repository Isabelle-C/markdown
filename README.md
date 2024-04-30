# mini-notebook

This serves as a toolkit box to do some basic file processing.

## Environment

- Managed with [Poetry](https://python-poetry.org/)

```bash
poetry install
```

## Usage

1. Activate environment

```bash
poetry shell
```

2. Run the script

`example`

```bash
python cli/markdown_to_word.py "example.md" "output.docx"
```

## Workflow
- Managed by Snakemake

`example` Edit config file and run script below to stretch the right margin of a PDF file.

```bash
snakemake --cores 1 -s ./snakemake/pdf_stretch.Snakefile
```