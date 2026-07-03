from google.cloud import speech
from google.cloud.speech import RecognitionAudio, RecognitionConfig
import subprocess
import os
from config import LANGUAGE_CODE


def convert_to_wav_ffmpeg(input_path, output_path="temp_audio.wav"):
    # Convert an audio file to WAV format using ffmpeg
    result = subprocess.run([
        "ffmpeg", "-y", "-i", input_path, "-ar", "16000", "-ac", "1", output_path
    ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if result.returncode != 0:
        raise RuntimeError(f"ffmpeg conversion error: {result.stderr.decode()}")

    return output_path


def transcribe_audio(audio_path):
    # Convert the file to wav
    wav_path = convert_to_wav_ffmpeg(audio_path)

    with open(wav_path, "rb") as audio_file:
        content = audio_file.read()

    if not content:
        raise ValueError("Audio file is empty or unreadable!")

    # Use the Google Speech API for transcription
    client = speech.SpeechClient()

    # Create the audio object for transcription
    audio = RecognitionAudio(content=content)

    # Configure the transcription (language, sample rate)
    config = RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        language_code=LANGUAGE_CODE,
        sample_rate_hertz=16000
    )
    # Call the API method for transcription
    response = client.recognize(config=config, audio=audio)

    # Join the received transcription results
    transcript = ""
    for result in response.results:
        transcript += result.alternatives[0].transcript + " "

    # Remove the temporary WAV file after transcription
    if os.path.exists(wav_path):
        os.remove(wav_path)

    return transcript.strip()
