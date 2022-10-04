from pytube import YouTube
    
def download_progress(stream,chunk, bytes_remaining ):
    bytes_downloaded = stream.filesize - bytes_remaining
    percent = bytes_downloaded*100//stream.filesize
    print(f"Progression du téléchargement {percent} %" )


def get_choice(min , max):
    choix_str = input(f"Quel choix est votre choix entre {min} et {max} : ")
    try:
        choix_int = int(choix_str)
    except ValueError:
        print("Veuillez entrer un nombre pas de lettres ;) ")
        return get_choice(min , max)
    else:
        if not min <= choix_int <= max:
            print(f"Veuillez saisir un nombre entre {min} et {max}")
            return get_choice(min,max)
    return choix_int

    
def download(url):
    video_youtube = YouTube(url)
    video_youtube.register_on_progress_callback(download_progress)
    print("Titre de la vidéo : "+video_youtube.title)
    NB_VUES = video_youtube.views
    print("Cette video a été vue : "+ str(NB_VUES) + " fois" )
    streams = video_youtube.streams.filter(progressive=True, file_extension="mp4")
    print("-----CHOIX DES RESOLUTIONS----")
    i = 1
    for stream in streams:
        print(f" {i} - {stream.resolution} ")
        i += 1
    choix = get_choice(1, len(streams))
    itag = streams[choix-1].itag
    select_stream = video_youtube.streams.get_by_itag(itag)
    print("telechargement...")
    select_stream.download("Video")
    print(f"La vidéo {video_youtube.title}  a été téléchargée")





