# Speech-to-text module
import whisper

# Load whisper model once
model = whisper.load_model("tiny")

def speech_to_text(audio_path):
    result = model.transcribe(audio_path)
    return result["text"]
