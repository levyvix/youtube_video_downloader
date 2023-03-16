from pytube import Playlist
import os
import sys


# make dir with playlistname
def download_playlist(link):
    p = Playlist(link)
    if not os.path.exists(p.title):
        os.mkdir(p.title)

    for i, video in enumerate(p.videos):
        print(video.title)
        # save to dir
        video.streams.get_highest_resolution().download(
            p.title, filename_prefix=str(i) + "_"
        )


if __name__ == "__main__":
    link = "https://www.youtube.com/playlist?list=PLo9Vi5B84_dfAuwJqNYG4XhZMrGTF3sBx"

    if len(sys.argv) > 1:
        link = sys.argv[1]

    download_playlist(link)
