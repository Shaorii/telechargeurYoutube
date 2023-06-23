from pytube import YouTube

def askVideoUrl() -> YouTube:
    while True:
        url = str(input("Url de la video:\n"))
        v = YouTube(url)
        try: 
            v.title # Crash if the playlist is invalid
            return v
        except:
            pass


def downloadVideo(video:YouTube, pauseWhenEnded=False) -> None:
    print()
    print(f"{video.title} - {video.length//60}:{video.length%60:02d}")
    print(video.watch_url)
    
    if video.age_restricted:
        print("La vidéo est soumise à une limite d'age")
        print("Tentative de contournement...")
        try:
            video.bypass_age_gate()
            print("Reussite")
        except:
            print("Echec")
    
    try:
        video.streams.filter(only_audio=True).first().download("telecharge/")
    except:
        print("Une erreur est survenue pendant le téléchargement")
        
    if pauseWhenEnded:
        print("FIN DU TELECHARGEMENT")
        input()