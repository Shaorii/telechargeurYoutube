import playlistDownload
import videoDownload

choix = -1
while -1 == choix:
    reponse = str(input("Video [1] ou playlist [2] ? (Appuyer sur ENTRER à la fin)\n"))
    if reponse.lower() in ("v", "1", "video", "vidéo"):
        choix = 1
    elif reponse.lower() in ("p", "2", "play", "playlist"):
        choix = 2
        
if 1 == choix:
    v = videoDownload.askVideoUrl()
    videoDownload.downloadVideo(v, True)
elif 2 == choix:
    p = playlistDownload.askPlaylistUrl()
    playlistDownload.downloadPlaylist(p)