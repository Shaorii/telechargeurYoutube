from pytube import Playlist
from videoDownload import downloadVideo


def askPlaylistUrl() -> Playlist:
    while True:
        url = str(input("Url de la playlist: (Appuyer sur ENTRER à la fin)\n"))
        try: 
            p = Playlist(url)
            p.title # Crash if the playlist is invalid
            return p
        except:
            pass


def downloadPlaylist(playlist: Playlist) -> None:
    for video in playlist.videos:
        downloadVideo(video)
    print("FIN DU TELECHARGEMENT (Appuyer sur ENTRER)")
    input()
