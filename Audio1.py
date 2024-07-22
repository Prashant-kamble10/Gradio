import gradio as gr
import speech_recognition as sr
from transformers import pipeline
import emoji

# Initialize the speech recognizer
recognizer = sr.Recognizer()

# Load the pipelines for summarization and sentiment analysis
summarizer = pipeline("summarization")
sentiment_analyzer = pipeline("sentiment-analysis")

# Function to transcribe audio to text
def transcribe_audio(audio_file):
    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Could not understand the audio"
    except sr.RequestError:
        return "Could not request results from Google Speech Recognition service"

# Function to summarize text
def summarize_text(text):
    summary = summarizer(text, max_length=50, min_length=25, do_sample=False)
    return summary[0]['summary_text']

# Function to analyze sentiment
def analyze_sentiment(text):
    sentiment = sentiment_analyzer(text)
    return sentiment[0]['label']

# Function to convert sentiment to emoji
def sentiment_to_emoji(sentiment):
    sentiment_emoji_map = {
        "POSITIVE": emoji.emojize(":smile:"),
        "NEGATIVE": emoji.emojize(":disappointed:"),
        "NEUTRAL": emoji.emojize(":neutral_face:")
    }
    return sentiment_emoji_map.get(sentiment, "")

# Main function to process audio file
def process_audio(audio_file):
    transcript = transcribe_audio(audio_file)
    summary = summarize_text(transcript)
    sentiment = analyze_sentiment(summary)
    sentiment_emoji = sentiment_to_emoji(sentiment)
    return transcript, summary, sentiment, sentiment_emoji

# Create Gradio interface
iface = gr.Interface(
    fn=process_audio,
    inputs=gr.Audio(source="microphone", type="filepath"),
    outputs=[
        gr.Textbox(label="Transcript"),
        gr.Textbox(label="Summary"),
        gr.Textbox(label="Sentiment"),
        gr.Textbox(label="Emoji")
    ],
    live=True
)

# Launch the interface
iface.launch()
