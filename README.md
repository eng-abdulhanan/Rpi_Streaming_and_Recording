# Rpi_Streaming_and_Recording
GUI application to stream on web server and record at different Resolutions

## Install MJPEG-STREAMER
Use following commands to install MJPEG-STREAMER on raspberry pi
```
sudo apt update -y
sudo apt upgrade -y
sudo apt install build-essential imagemagick libv4l-dev libjpeg-dev cmake -y
cd /tmp
git clone https://github.com/jacksonliam/mjpg-streamer.git
cd mjpg-streamer/mjpg-streamer-experimental
sudo make
sudo make install
```
## Install FMJPEG 
Install FMJPEG to record stream from web server.
```
sudo apt update -y
sudo apt install ffmpeg -y
```
## MJPEG-STREAMER Bash Script
Download **mjpeg.sh** file from code directory and make it executeable by following command
```
sudo chmod +x mjpeg.sh
```
