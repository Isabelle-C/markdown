import fitz

class Pdf:
    def __init__(self, path):
        self.path = path
    
    def add_right_margin(self, output_pdf_path, extra_margin):
        # Open the input PDF
        doc = fitz.open(self.path)

        # Create a new PDF for the output
        new_doc = fitz.open()

        for page in doc:
            # Get the size of the original page
            original_rect = page.rect

            # Create a new, larger page size by adding extra margin to the width
            new_rect = fitz.Rect(0, 0, original_rect.width + extra_margin, original_rect.height)

            # Add a new page to the output document with the larger size
            new_page = new_doc.new_page(width=new_rect.width, height=new_rect.height)

            # Create a new rectangle for the original page content, shifted to the left
            content_rect = fitz.Rect(0, 0, original_rect.width, original_rect.height)

            # Show the original page content in the new rectangle
            new_page.show_pdf_page(content_rect, doc, page.number)

        # Save the output PDF with the added margins
        new_doc.save(output_pdf_path)

        # Close the documents
        doc.close()
        new_doc.close()
