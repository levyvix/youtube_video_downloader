from pytube import Playlist
from pathlib import Path


def download_all_videos(p_link, path):
    playlist = Playlist(p_link)
    path_for_playlist = path / playlist.title
    for id, video in enumerate(playlist.videos):
        print("Downloading: ", video.title)

        vid = (
            video.streams.filter(progressive=True, file_extension="mp4")
            .order_by("resolution")
            .desc()
            .first()
        )

        # downloads video in sequence, and adds a ID prefix
        try:
            vid.download(output_path=path_for_playlist, filename=f"{id+1}_{vid.title}")

        except Exception as e:
            print("Something wrong happened :(", e)

        print(f"Downloaded {vid.title}! \n")


if __name__ == "__main__":
    playlist_dir = Path("./playlists")
    playlist_link = "https://www.youtube.com/watch?v=Mph0cWZsoV4&list=PLM8lYG2MzHmQn55ii0duXdO9QSoDF5myF"

    download_all_videos(playlist_link, playlist_dir)
