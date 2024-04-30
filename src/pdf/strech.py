  # Import the PyMuPDF library

def add_margins_to_pdf(input_pdf_path, output_pdf_path, extra_margin=100):
    """
    Adds extra margins to each page of a PDF.
    
    Parameters:
    - input_pdf_path: Path to the input PDF file.
    - output_pdf_path: Path where the output PDF with extra margins will be saved.
    - extra_margin: Size of the extra margin to add on each side (in points).
    """
    # Open the input PDF
    doc = fitz.open(input_pdf_path)
    
    # Create a new PDF for the output
    new_doc = fitz.open()
    
    for page in doc:  # Iterate through each page of the input PDF
        # Get the original page size
        original_rect = page.rect
        
        # Create a new, larger page size by adding extra margin to the width
        new_rect = fitz.Rect(0, 0, original_rect.width + extra_margin, original_rect.height)

        # Add a new page to the output document with the larger size
        new_page = new_doc.new_page(width=new_rect.width, height=new_rect.height)
        
        # Place the original page content in the center of the new page
        new_page.show_pdf_page(new_rect, doc, page.number)
    
    # Save the output PDF with the added margins
    new_doc.save(output_pdf_path)
    
    # Close the documents
    doc.close()
    new_doc.close()



# Example usage
input_pdf_path = "/Users/isabellechen/Desktop/jarvis_lab/papers/4.pdf"  # Update this path
output_pdf_path = "/Users/isabellechen/Desktop/jarvis_lab/papers/42.pdf"  # Update this path
extra_margin = 250  # Update this value
add_right_margin(input_pdf_path, output_pdf_path, extra_margin)
