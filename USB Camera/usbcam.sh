#!/bin/bash
# sudo apt-get install fswebcam
# sudo nano usbcam.sh
# chmod +x usbcam.sh
# ./usbcam.sh
CURRENT_DATE=$(date +"%Y-%m-%d_%H%M")
fswebcam -r 1280x720 --no-banner /home/pi/img_$CURRENT_DATE.jpg
fswebcam --delay 2 -r 640x480 --timestamp "%d-%m-%Y %H:%M:%S" /home/pi/img2_"%d-%m-%Y %H:%M:%S".jpg
