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

    if link := '':
        download(link, home_dir)
    else:
        # open the videos.txt with the videos and download one by one

        with open('./videos.txt', 'rb') as videos:
            videos = videos.readlines()

        for v in videos:
            download(v.decode('utf-8'), home_dir)
