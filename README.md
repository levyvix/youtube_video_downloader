# Youtube Video Downloader

## Using pytube to download videos and playlists from Youtube

### How to use

- clone the repo
- install the requirements `pip install -r requirements.txt`

#### Download Videos

- You can run the command passing the video as a argument. Like this: `python video_download.py https://www.youtube.com/watch?v=1234`
- Or if you want to download more than one video at a time, you can change the `videos.txt` file and add all the youtube links, one by one, each line at a time, and then in the `video_download.py` script, change the file flag to `True`.

#### Download Playlists

- You can run the command passing the playlist as a argument. Like this: `python playlist_download.py https://www.youtube.com/watch?v=Mph0cWZsoV4&list=1234`

### Where are the videos downloaded?

- The videos will be downloaded in the `Videos` folder
- The playlists will be downloaded in the `Playlists` folder

### TODO

- [X] Add a progress bar
- [X] Add a way to download the videos in the best quality
- [ ] Make a CLI
