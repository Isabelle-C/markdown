import sys

import pypandoc

def markdown_to_word(markdown_file_path, output_file_path):
    """
    Convert a Markdown file to a Word document.
    
    Args:
    markdown_file_path (str): The path to the Markdown file.
    output_file_path (str): The path where the Word file will be saved.
    """
    output = pypandoc.convert_file(markdown_file_path, 'docx', outputfile=output_file_path)
    return output

if __name__ == '__main__':
    markdown_to_word(sys.argv[1], sys.argv[2])
