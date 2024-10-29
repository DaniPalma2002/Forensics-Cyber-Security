import PyPDF2
import re

def extract_words_from_pdf(pdf_path, output_txt_path):
    with open(pdf_path, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        all_text = ""
        
        # Extract text from each page of the PDF
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            all_text += page.extract_text()

        # Use regex to find all words
        words = re.findall(r'\b\w+\b', all_text)

        # Write words, each on a new line
        with open(output_txt_path, 'w') as output_file:
            for word in words:
                output_file.write(word + '\n')

# Usage
pdf_path = "thrones.pdf"  # Replace with your PDF file path
output_txt_path = "output_words.txt"  # Replace with your desired output text file path
extract_words_from_pdf(pdf_path, output_txt_path)
