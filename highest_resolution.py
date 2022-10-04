from pytube import YouTube
import ffmpeg
import os

def download_progress(stream,chunk, bytes_remaining ):
    bytes_downloaded = stream.filesize - bytes_remaining
    percent = bytes_downloaded*100//stream.filesize
    print(f"Progression du téléchargement {percent} %" )

def download_highest_resolution(url):
    video_youtube = YouTube(url)
    video_youtube.register_on_progress_callback(download_progress)
    print("Titre de la vidéo : "+video_youtube.title)
    NB_VUES = video_youtube.views
    print("Cette video a été vue : "+ str(NB_VUES) + " fois" )
    streams = video_youtube.streams.filter(progressive=False, file_extension='mp4', type="video").order_by('resolution').desc()
    video_stream = streams[0]
    streams = video_youtube.streams.filter(progressive=False, file_extension='mp4', type="audio").order_by('abr').desc()
    audio_stream = streams[0]
    print("Téléchargement de La vidéo")
    video_stream.download("video")
    print("Téléchargement de L'audio")
    audio_stream.download("audio")
    print("Combinaison des deux fichiers")
    audio_filename = os.path.join("audio", video_stream.default_filename)
    video_filename = os.path.join("video", video_stream.default_filename)
    output_filename = video_stream.default_filename
    ffmpeg.output(ffmpeg.input(audio_filename), ffmpeg.input(video_filename), output_filename, vcodec="copy", acodec="copy", loglevel="quiet").run(overwrite_output=True)
    os.remove(audio_filename)
    os.remove(video_filename)
    os.rmdir("audio")
    os.rmdir("video")
    print(f"La vidéo avec la meilleure resolution {video_youtube.title}  a été téléchargée")
