from google.cloud import speech, texttospeech
import openai

openai.api_key = "22ec84421ec24230a3638d1b51e3a7dc"

def transcribe_audio(audio_path):
    client = speech.SpeechClient()

    with open(audio_path, "rb") as audio_file:
        audio_content = audio_file.read()

    audio = speech.RecognitionAudio(content=audio_content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="en-US"
    )

    response = client.recognize(config=config, audio=audio)
    transcript = " ".join(result.alternatives[0].transcript for result in response.results)
    return transcript

def correct_transcription(transcript):
    response = openai.ChatCompletion.create(
        engine="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that corrects text."},
            {"role": "user", "content": transcript}
        ]
    )
    corrected_text = response.choices[0].message['content']
    return corrected_text

def generate_speech(text, output_audio_path="corrected_audio.mp3"):
    client = texttospeech.TextToSpeechClient()

    input_text = texttospeech.SynthesisInput(text=text)
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        name="en-US-JourneyNeural"
    )
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    response = client.synthesize_speech(
        input=input_text, voice=voice, audio_config=audio_config
    )

    with open(output_audio_path, "wb") as out:
        out.write(response.audio_content)
    return output_audio_path
