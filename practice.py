# import gradio as gr

# def practice(name):
#     return "Namsate" + " " +  name

# Iface = gr.Interface(fn = practice, inputs= "text", outputs="text")
# Iface.launch()
# ------------------------------------------------------------------------------------------------------------------------------------

# import gradio as gr

# def practice(name):
#     return "Namsate" + " " +  name

# Iface = gr.Interface(fn = practice, 
#                      inputs= gr.Textbox(lines= 10, placeholder="Enter your address here"), 
#                      outputs= gr.Textbox(lines= 5, placeholder="Expext output here"))
# Iface.launch(debug=True)
# ------------------------------------------------------------------------------------------------------------------------------------

#  gradio code that takes table data as input, and table as output.
# import gradio as gr
# import pandas as pd

# def process_table(data):
#     # Convert the input list of lists to a pandas DataFrame
#     df = pd.DataFrame(data)
    
#     # Example processing: Add a new column that is the sum of the first two columns
#     if df.shape[1] >= 2:  # Ensure there are at least two columns
#         df['Sum'] = df.iloc[:, 0] + df.iloc[:, 1]
    
#     # Return the processed DataFrame
#     return df

# # Define the input and output components
# inputs = gr.DataFrame(headers=["Column 1", "Column 2"], label="Input Table")
# outputs = gr.DataFrame(label="Output Table")

# # Create the Gradio interface
# iface = gr.Interface(fn=process_table, inputs=inputs, outputs=outputs)

# # Launch the interface
# iface.launch(share=True)
# ------------------------------------------------------------------------------------------------------------------------------------

# in input it should take text, audio, pdf,

# and in output it should give text, table, emoji, pdf.

# import gradio as gr
# import pandas as pd
# from fpdf import FPDF

# def process_inputs(text_input, audio_input, pdf_input):
#     # Process text input
#     processed_text = f"Received text: {text_input}"
    
#     # Process audio input
#     transcribed_text = "Transcribed audio (example text)"
    
#     # Process PDF input
#     pdf_summary = "PDF summary (example text)"
    
#     # Generate a simple data table from the inputs
#     data = {
#         "Input Type": ["Text", "Audio", "PDF"],
#         "Content": [text_input, "Audio content", "PDF content"],
#     }
#     table = pd.DataFrame(data)
    
#     # Generate an emoji based on the text input
#     emoji = "😊" if "happy" in text_input.lower() else "😐"
    
#     # Generate a PDF file as output
#     pdf = FPDF()
#     pdf.add_page()
#     pdf.set_font("Arial", size=12)
#     pdf.cell(200, 10, txt="Generated PDF from Inputs", ln=True)
#     pdf.cell(200, 10, txt=processed_text, ln=True)
#     pdf.cell(200, 10, txt=transcribed_text, ln=True)
#     pdf.cell(200, 10, txt=pdf_summary, ln=True)
#     pdf_output = "/mnt/data/output.pdf"
#     pdf.output(pdf_output)
    
#     return processed_text, table, emoji, pdf_output

# # Define the inputs and outputs
# inputs = [
#     gr.Textbox(label="Text Input"),
#     gr.Audio(label="Audio Input"),
#     gr.File(label="PDF Input", file_count="single", type="file")
# ]

# outputs = [
#     gr.Textbox(label="Processed Text"),
#     gr.Dataframe(label="Data Table"),
#     gr.Textbox(label="Emoji"),
#     gr.File(label="Generated PDF")
# ]

# # Create the Gradio interface
# iface = gr.Interface(fn=process_inputs, inputs=inputs, outputs=outputs)

# # Launch the interface
# iface.launch(share=True)
# ------------------------------------------------------------------------------------------------------------------------------------

# import gradio as gr
# import PyPDF2
# from docx import Document
# import tempfile

# def process_pdfs_and_query(pdfs, query):
#     # Initialize a Document
#     document = Document()
    
#     # Process each PDF file
#     for pdf in pdfs:
#         reader = PyPDF2.PdfReader(pdf.name)
#         for page in reader.pages:
#             text = page.extract_text()
#             if query.lower() in text.lower():
#                 document.add_paragraph(text)
    
#     # Save the Word document to a temporary file
#     temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".docx")
#     document.save(temp_file.name)
#     temp_file.close()
    
#     return temp_file.name

# # Create the Gradio Interface
# iface = gr.Interface(
#     fn=process_pdfs_and_query,
#     inputs=[gr.File(label="Upload PDF Files", file_count="multiple"), 
#             gr.Textbox(label="Enter Query")],
#     outputs=gr.File(label="Generated Word Document"),
#     title="PDF to Word with Query"
# )

# # Launch the interface
# iface.launch()

# ------------------------------------------------------------------------------------------------------------------------------------
import gradio as gr
import os

def process_files_and_query(files, query):
    # Your logic to process files and query goes here
    # Ensure that the generated file exists and the path is correct

    # For example purposes, assuming the document is created and saved in the current directory
    output_path = "generated_document.docx"  # Replace this with actual file creation logic

    # Check if the file exists
    if os.path.exists(output_path):
        return output_path
    else:
        return None  # Handle this case in your Gradio interface

with gr.Blocks(css="""
    .gradio-container {background-color: #183658 !important; color: white !important;}
    .gr-button.generate-button {background-color: orange !important; color: white !important;}
    textarea, input[type="file"] {
        width: 100%;
        height: auto;  /* Adjusted for auto height */
    }
    .file-input-container {
        width: 50%;  /* 50% of the row */
    }
    .query-input-container {
        width: 50%;  /* 50% of the row */
        display: flex;
        flex-direction: column;
        height: 100vh;
    }
    .query-input-container .gr-textbox {
        flex-grow: 1;
    }
    .query-input-container .generate-button-container {
        flex-shrink: 0;
    }
""") as demo:
    with gr.Row():
        with gr.Column(scale=1, elem_id="file-input-container"):
            file_inputs = gr.File(label="Upload Files", file_count="multiple")
        with gr.Column(scale=1, elem_id="query-input-container"):
            query_input = gr.Textbox(label="Enter your Query", lines=10)
            generate_button = gr.Button("Generate", elem_id="generate-button")
            output_file = gr.File(label="Generated Document", interactive=False)

    generate_button.click(fn=process_files_and_query, inputs=[file_inputs, query_input], outputs=output_file)

demo.launch(debug=True)






# ------------------------------------------------------------------------------------------------------------------------------------
# how to use flagged folder for the project


# import pandas as pd

# pd.read_csv("copy path flagged folder path here")
# ------------------------------------------------------------------------------------------------------------------------------------
