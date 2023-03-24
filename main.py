from pytube import YouTube, Playlist

def singleVideo():
    url = input("Introduce the video url: ")
    video = YouTube(url) 
    streams = video.streams.filter(progressive=True)
    print("Select the video resolution:")
    for i, stream in enumerate(streams):
        print(f"{i+1}. {stream.resolution}")
    choice = int(input())
    stream = streams[choice-1]
    stream.download()

def playlist():
    playlist_url = input("intoduce the playlist url: ")
    playlist = Playlist(playlist_url)
    for video_url in playlist.video_urls:
        video = YouTube(video_url)
        stream = video.streams.get_highest_resolution()
        print(f"Downlading {video.title}...")
        stream.download()
def justAudio():
    url = input("intoduce the url to download the audio")
    yt = YouTube(url)
    audio = yt.streams.filter(only_audio=True).first()
    audio.download(output_path=".", filename=yt.title + ".mp4")
    print("Descarga completada!")

boolMenu = True
while boolMenu == True:
    print("------------------------")
    print("WELCOME TO YT_DOWNLOADER")
    print("     BY ManuNunez")
    print("------------------------")
    print("select a option to download")
    print("1) Download a single video")
    print("2) Download a list of videos")
    print("3) Download just audio")
    print("4) Exit")
    option = int(input())
    if option == 1:
        singleVideo()
    elif option == 2:
        playlist()
    elif option == 3:
        justAudio()
    elif option == 4:
        boolMenu == False
    else:
        print("{} is not a valid option" .format(option))
