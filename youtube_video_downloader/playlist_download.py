import sys
from pathlib import Path
import typer
from pytube import Playlist


app = typer.Typer()


# make dir with playlistname
def download_playlist(link: str, path: Path):
    p = Playlist(link)
    to_path = path / p.title

    for i, video in enumerate(p.videos):
        print(video.title)
        # save to dir
        video.streams.get_highest_resolution().download(
            to_path,
            filename_prefix=str(i) + "_",
        )


@app.command()
def download(
    link: str = "https://www.youtube.com/playlist?list=PLo9Vi5B84_dfAuwJqNYG4XhZMrGTF3sBx",
    path: Path = Path("./Playlists"),
):
    """
    Downloads a YouTube playlist to the specified path.

    Args:
        link (str): The link of the YouTube playlist to be downloaded. Defaults to "https://www.youtube.com/playlist?list=PLo9Vi5B84_dfAuwJqNYG4XhZMrGTF3sBx".
        path (Path): The path where the playlist will be saved. Defaults to "./Playlists".

    Returns:
        None

    This function uses the pytube library to download the playlist from the given link. It creates a directory with the playlist's title and saves each video in the playlist to that directory. The videos are saved with a prefix indicating their order in the playlist.

    Example:
        >>> download("https://www.youtube.com/playlist?list=PLo9Vi5B84_dfAuwJqNYG4XhZMrGTF3sBx", Path("./Playlists"))
        Downloading Video: Video Title 1
        Downloading Video: Video Title 2
        ...
    """
    link = sys.argv[1]

    download_playlist(link, path)


if __name__ == "__main__":
    app()
