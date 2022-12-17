from pytube import YouTube
from pathlib import Path


def download(video_link, path):
    yt = YouTube(video_link)
    print("Downloading Video: ", yt.title)
    video = yt.streams.get_highest_resolution()
    video.download(output_path=path)
    print("Video Donwloaded: ", yt.title)


if __name__ == '__main__':
    home_dir = Path('./videos')
    link = 'https://www.youtube.com/watch?v=u31mTpus12k'
    download(link, home_dir)
