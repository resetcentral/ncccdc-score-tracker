# CCDC Score Tracker

This is a simple tool hacked together in an afternoon made to scrape the livestream for [NCCCDC](dakotacon.org).

## Dependencies
* [Youtube-dl](https://ytdl-org.github.io/youtube-dl/index.html)
* [Streamlink](https://github.com/streamlink/streamlink)
* [Python Image Library](https://pypi.org/project/PIL/)

## Usage

The tools works in three steps.

1. Download the video
2. Extract the frames from the video (1/sec)
3. Analyze the each frame to determine the status of services

To use the tool:

* Run `./get_url.sh <youtube_url>` to retrieve the HLS URL for the livestream.
* Edit `download_video.sh` to use that URL.
* Run `./download_video.sh`. The script will continuously download from the livestream until you hit CTRL+C.
* Run `./extract_frames.sh <path_to_video>`
* Run `./calc_scores.py`
* Run `./total_scores.py` to view service uptime by team.

You'll want to run `download_video.sh` for a short time to get some sample images in order to fill out `config.json`. In that file you need:

* `origin`: The pixel coordinates of the top-left most service check (X or check mark)
* `x_space`: The x-spacing between service checks
* `y_space`: The y-spacing between service checks
* `teams`: The number of teams
* `services`: The number of services

If you missed a portion of the livestream, you can add the `--hls-live-edge <num_segments>` option to the `streamlink` command in `download_video.sh` start the download from before the current time.
