from pytube import Playlist
import os
import sys
from pathlib import Path


# make dir with playlistname
def download_playlist(link, path):
    p = Playlist(link)
    to_path = path / p.title

    for i, video in enumerate(p.videos):
        print(video.title)
        # save to dir
        video.streams.get_highest_resolution().download(
            to_path,
            filename_prefix=str(i) + "_",
        )


if __name__ == "__main__":
    path = Path("./Playlists")
    link = "https://www.youtube.com/playlist?list=PLo9Vi5B84_dfAuwJqNYG4XhZMrGTF3sBx"

    if len(sys.argv) > 1:
        link = sys.argv[1]

    download_playlist(link, path)
