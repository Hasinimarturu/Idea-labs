from moviepy.editor import VideoFileClip, AudioFileClip

def extract_audio(video_path):
    video = VideoFileClip(video_path)
    audio_path = "extracted_audio.wav"
    video.audio.write_audiofile(audio_path)
    return audio_path

def replace_audio_in_video(video_path, new_audio_path, output_video_path="final_output_video.mp4"):
    video = VideoFileClip(video_path)
    audio = AudioFileClip(new_audio_path)
    new_video = video.set_audio(audio)
    new_video.write_videofile(output_video_path, codec="libx264", audio_codec="aac")
    return output_video_path
