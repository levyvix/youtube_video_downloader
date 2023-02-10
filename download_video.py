import sys
from pathlib import Path

import pytube

# add a progess bar


def on_progress(stream, chunk, bytes_remaining):

    total = round(stream.filesize / 1024 / 1024, 2)
    remaining = round(bytes_remaining / 1024 / 1024, 2)

    # show percentage
    print(f"{round((total - remaining) / total * 100, 2)}%")


def on_complete(stream: pytube.Stream, file_path: str):
    print("Download Complete! Saving to: ", file_path)


def download(video_link, path):
    # add a progress bar
    yt = pytube.YouTube(video_link, on_progress_callback=on_progress, on_complete_callback=on_complete)
    print("Downloading Video: ", yt.title)
    video = yt.streams.get_by_itag(22)

    # add a progess bar
    video.download(output_path=path)

    print("Video Donwloaded: ", yt.title)


if __name__ == "__main__":
    home_dir = Path("./videos")
    link = "https://www.youtube.com/watch?v=uKyojQjbx4c"

    # if a video link is passed as an argument, use it
    if len(sys.argv) > 1:
        link = sys.argv[1]

        download(link, home_dir)
    elif len(sys.argv) == 1:
        download(link, home_dir)

    else:
        # open the videos.txt with the videos and download one by one

        with open("./videos.txt", "rb") as videos:
            videos = videos.readlines()

            for v in videos:
                download(v.decode("utf-8"), home_dir)
