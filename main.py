import Youtubedownloader
import audio_Youtube_downloader
import highest_resolution

def get_url():
    url = input("Donnez l'url de votre vidéo : ")
    if check_url(url):
        print("URL VALIDE")
        return url
    print("URL INVALIDE\nVeuillez saisir une URL YOUTUBE VALIDE")
    return get_url()

def check_url(url):
    if url.lower().startswith("https://www.youtube.com/"):
        return True
    return False

while True:
    print("""
    ---------------------------- Menu de commande ----------------------------
    1-Pour utiliser ce programme
    2-Quitter
    """)
    choix_menu = Youtubedownloader.get_choice(1,2)

    match (choix_menu):

        case 1 :
            print("""
        --------------------------------------------- BIENVENUE DANS YOUTUBE DOWNLOADER TOTAL ---------------------------------------------

        Vous voulez télécharger :
        1-Une video avec une résolution de votre choix (360p et 720p)
        2-Un audio
        3-Une vidéo avec la meilleure résolution possible
        """)
            choice = Youtubedownloader.get_choice(1,3)
            match (choice):
                case 1:
                    Youtubedownloader.download(get_url())
                case 2:
                    audio_Youtube_downloader.download_audio(get_url())
                case 3:
                    highest_resolution.download_highest_resolution(get_url())
        case 2:
            print("Fin du programme")
            exit()
