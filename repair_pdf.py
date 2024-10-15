import fitz  # PyMuPDF

def repair_pdf(input_path, output_path):
    document = fitz.open(input_path)
    document.save(output_path, garbage=4, deflate=True)
    document.close()