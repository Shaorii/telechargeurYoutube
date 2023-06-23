from pytube import YouTube
from moviepy.editor import AudioFileClip
from os import remove

def askVideoUrl() -> YouTube:
    while True:
        url = str(input("Url de la video: (Appuyer sur ENTRER à la fin)\n"))
        try: 
            v = YouTube(url)
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
        path = video.streams.filter(only_audio=True).first().download("telecharge/")
    except:
        print("Une erreur est survenue pendant le téléchargement")
        
    try:
        convertVideo(path)
    except:
        print("Une erreur est survenue pendant la conversion en mp3")
        
    if pauseWhenEnded:
        print("FIN DU TELECHARGEMENT (Appuyer sur ENTRER)")
        input()
        
        
def convertVideo(path: str) -> None:
    print("Conversion en mp3...")
    vid = AudioFileClip(path)
    # We suppose that path is ending by .mp4
    vid.write_audiofile(path[:-1]+"3")
    
    remove(path)