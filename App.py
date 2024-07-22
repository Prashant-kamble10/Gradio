import gradio as gr

# Define a function that returns the hardcoded response
def chatbot(input_text):
    # Hardcoded prompts and responses
    responses = {
        "Hello, how can I help you today?": "I am here to assist you with any queries you have.",
        "What is your name?": "I am a simple hardcoded chatbot.",
        "How does this work?": "You type a prompt, and I respond with a hardcoded answer.",
        "Goodbye!": "Have a great day!",
        "prashant":"Kamble"
    }

    # Check if the input matches any of the prompts
    if input_text in responses:
        return responses[input_text]
    else:
        return "Sorry, I can only respond to specific prompts."

# Create the Gradio interface
iface = gr.Interface(
    fn=chatbot, 
    inputs="text", 
    outputs="text",
    title="Hardcoded Chatbot",
    description="This is a simple chatbot with multiple hardcoded prompts and responses."
)

# Launch the interface
iface.launch()
