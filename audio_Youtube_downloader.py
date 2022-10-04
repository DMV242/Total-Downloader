from pytube import YouTube
import os
from pathlib import Path

def download_progress(stream,chunk, bytes_remaining ):
    bytes_downloaded = stream.filesize - bytes_remaining
    percent = bytes_downloaded*100//stream.filesize
    print(f"Progression du téléchargement {percent} %" )


def download_audio(url):
    video_youtube = YouTube(url)
    video_youtube.register_on_progress_callback(download_progress)
    print("Titre de la vidéo : "+video_youtube.title)
    NB_VUES = video_youtube.views
    print("Cette video a été vue : "+ str(NB_VUES) + " fois" )
    audio_stream = video_youtube.streams.get_audio_only()
    print("telechargement...")
    audio_stream.download("audio")
    p = Path(os.path.join("audio", audio_stream.default_filename))
    p.rename(p.with_suffix('.mp3'))
    print(f"L'audio {video_youtube.title}  a été téléchargée")