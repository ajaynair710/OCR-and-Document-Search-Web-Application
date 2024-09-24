import gradio as gr
import pytesseract
from PIL import Image
import json

# Set up Tesseract path if necessary (Update the path based on your installation)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def process_image(image):
    # Perform OCR using Tesseract
    extracted_text = pytesseract.image_to_string(image, lang='eng+hin')
    
    # Return extracted text
    return extracted_text.strip()

def search_keywords(text, keyword):
    # Search for the keyword in the extracted text
    matches = []
    for line in text.splitlines():
        if keyword.lower() in line.lower():
            matches.append(line)

    return matches

def create_interface():
    with gr.Blocks() as demo:
        gr.Markdown("# OCR and Document Search Web Application")
        gr.Markdown("Upload an image containing Hindi or English text for OCR processing.")
        
        image_input = gr.Image(type="pil", label="Upload Image")
        output_text = gr.Textbox(label="Extracted Text", interactive=False, lines=10)
        
        keyword_input = gr.Textbox(label="Enter Keyword", placeholder="Type keyword to search...")
        search_output = gr.Textbox(label="Search Results", interactive=False, lines=5)
        
        submit_btn = gr.Button("Process Image")
        search_btn = gr.Button("Search Keyword")
        
        # Define button actions
        submit_btn.click(process_image, inputs=image_input, outputs=output_text)
        search_btn.click(search_keywords, inputs=[output_text, keyword_input], outputs=search_output)
    
    return demo

# Run the web application
if __name__ == "__main__":
    app = create_interface()
    app.launch(share=True)  # Set share=True to create a public link
