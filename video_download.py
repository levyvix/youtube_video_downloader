import sys
from pathlib import Path

import pytube


def download(video_link, path):
    # add a progress bar
    yt = pytube.YouTube(video_link, on_progress_callback=progress_func)
    print("Downloading Video: ", yt.title)
    video = yt.streams.get_by_itag(22)  # 720p

    video.download(output_path=path)

    print("\nVideo Donwloaded: ", yt.title)


def progress_func(stream, chunk, bytes_remaining):
    curr = stream.filesize - bytes_remaining
    done = int(50 * curr / stream.filesize)
    sys.stdout.write("\r[{}{}] ".format("=" * done, " " * (50 - done)))
    sys.stdout.flush()


if __name__ == "__main__":
    path = Path("./Videos")
    link = "https://www.youtube.com/watch?v=uKyojQjbx4c"
    file = True

    # if a video link is passed as an argument, use it
    if len(sys.argv) > 1:
        link = sys.argv[1]

        download(link, path)

    elif file:
        # open the videos.txt with the videos and download one by one

        with open("./videos.txt", "rb") as videos:
            videos = videos.readlines()

            for v in videos:
                download(v.decode("utf-8"), path)

    else:
        download(link, path)
