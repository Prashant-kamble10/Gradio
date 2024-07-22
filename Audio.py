import gradio as gr
import speech_recognition as sr

def transcribe_audio(audio):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio) as source:
        audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data)
    return text

iface = gr.Interface(
    fn=transcribe_audio,
    inputs=gr.Audio(type="filepath"),
    outputs="text",
    title="Audio to Text Transcription",
    description="Upload an audio file and get its transcription."
)

iface.launch()


# import gradio as gr
# import speech_recognition as sr

# def transcribe_audio(audio):
#     recognizer = sr.Recognizer()
#     with sr.AudioFile(audio) as source:
#         audio_data = recognizer.record(source)
#         text = recognizer.recognize_google(audio_data)
#     return text

# css = """
# .gradio-container {
#     display: flex;
#     flex-direction: column;
#     align-items: center;
# }
# """

# iface = gr.Interface(
#     fn=transcribe_audio,
#     inputs=gr.Audio(type="filepath"),
#     outputs="text",
#     title="Audio to Text Transcription",
#     description="Upload an audio file and get its transcription.",
#     css=css
# )

# iface.launch()




