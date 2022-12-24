from pytube import Playlist
from pathlib import Path


def download_all_videos(p_link, path):

    playlist = Playlist(p_link)
    path_for_playlist = path/playlist.title
    for video in playlist.videos:
        print("Downloading: ", video.title)

        video.streams.get_highest_resolution().download(output_path=path_for_playlist)

        print(f"Downloaded {video.title}! \n")


if __name__ == '__main__':
    playlist_dir = Path('./playlists')
    playlist_link = 'https://www.youtube.com/watch?v=Mph0cWZsoV4&list=PLM8lYG2MzHmQn55ii0duXdO9QSoDF5myF'
    

    download_all_videos(playlist_link)
