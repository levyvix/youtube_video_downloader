# Youtube Video Downloader

## Using pytube to download videos and playlists from Youtube


### How to use
- clone the repo
- install the requirements `pip install -r requirements.txt`

#### Download Videos

- If you want to download a video, you can modify the `download_video.py` script, and add the link to the video. 
- Or if you want to download more than one video at a time, you can change the `videos.txt` file and add all the youtube links, one by one, each line at a time.
- Or you can run the command passing the video as a argument. Like this: `python download_playlist.py https://www.youtube.com/watch?v=1234`

#### Download Playlists
- If you want to download an entire playlist, you can modify the `download_playlist.py`, and add the link to the playlist
- Or you can run the command passing the playlist as a argument. Like this: `python download_video.py https://www.youtube.com/watch?v=Mph0cWZsoV4&list=1234`

### Where are the videos downloaded?
- The videos will be downloaded in the `Videos` folder
- The playlists will be downloaded in the `Playlists` folder



### TODO
- [ ] Add a progress bar
- [ ] Add a GUI
- [X] Add a way to download the videos in the best quality