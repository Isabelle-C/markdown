import pypandoc

class MarkDown:
    def __init__(self, file: str):
        """
        Initialize the MarkDown class.

        Parameters
        ----------
        file : str
            The path to the Markdown file.
        """
        self.file = file

    def to_word(self, output_file_path: str):
        """
        Convert a Markdown file to a Word document.
        
        Parameters
        ----------
        output_file_path : str 
            The path where the Word file will be saved.
        """
        output = pypandoc.convert_file(self.file, 'docx', outputfile=output_file_path)
        return output

    def to_pdf(self, output_file_path: str):
        """
        Convert a Markdown file to a PDF document.
        
        Parameters
        ----------
        output_file_path : str
            The path where the PDF file will be saved.
        """
        output = pypandoc.convert_file(self.file, 'pdf', outputfile=output_file_path)
        return output
