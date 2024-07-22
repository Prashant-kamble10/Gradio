import speech_recognition as sr

def main():

    sound = "harvard.wav"

    r = sr.Recognizer()

    with sr.AudioFile(sound) as source:
        r.adjust_for_ambient_noise(source)

        print("Audio converting to text......")

        audio = r.listen(source)


        try:
            print("converted audio is : \n" + r.recognize_google(audio)) 

        except Exception as e:
            print(e)


if __name__ == "__main__" :
    main()


import gradio as gr
import speech_recognition as sr

def transcribe_audio(audio_file):
    r = sr.Recognizer()
    
    # Convert file path to an actual file-like object
    with sr.AudioFile(audio_file) as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

        try:
            # Transcribe the audio to text using Google's API
            text = r.recognize_google(audio)
        except sr.UnknownValueError:
            text = "Google Speech Recognition could not understand the audio."
        except sr.RequestError:
            text = "Could not request results from Google Speech Recognition service."
        except Exception as e:
            text = str(e)

    return text

# Create the Gradio interface
interface = gr.Interface(
    fn=transcribe_audio,
    inputs=gr.Audio(type="filepath"),
    outputs="text",
    title="Audio Transcription",
    description="Upload an audio file to get its transcription."
)

# Launch the interface
if __name__ == "__main__":
    interface.launch()

