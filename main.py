import streamlit as st
from audio_utils import extract_audio, replace_audio_in_video
from ai_services import transcribe_audio, correct_transcription, generate_speech

st.title('Video Audio Replacement with AI-Generated Voice')
st.write("Upload a video file, and we'll replace its audio with an AI-generated voice.")

uploaded_file = st.file_uploader("Upload a video file", type=["mp4", "mov", "avi"])

if uploaded_file is not None:
    with open("input_video.mp4", "wb") as f:
        f.write(uploaded_file.read())
    st.video("input_video.mp4")

    # Step 1: Extract audio from the video
    audio_file = extract_audio("input_video.mp4")
    
    # Step 2: Transcribe the audio using Google’s Speech-to-Text API
    transcription = transcribe_audio(audio_file)
    st.write("Original transcription:")
    st.write(transcription)

    # Step 3: Correct the transcription using GPT-4o
    corrected_transcription = correct_transcription(transcription)
    st.write("Corrected transcription:")
    st.write(corrected_transcription)

    # Step 4: Convert corrected transcription back into speech
    generated_audio = generate_speech(corrected_transcription)
    
    # Step 5: Replace original audio in the video
    final_video = replace_audio_in_video("input_video.mp4", generated_audio)
    st.video(final_video)
