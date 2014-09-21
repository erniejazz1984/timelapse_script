#ffmpeg -r 30 %04d.JPG -s hd480 -vcodec libx264 hq time-lapse.mp4
avconv -y -r 15 -i D_%04d.JPG  -vcodec libx264 -q:v 1  timelapse.mp4;

