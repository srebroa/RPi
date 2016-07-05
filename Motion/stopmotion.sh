#!/bin/bash
#sudo /etc/init.d/motion stop
sudo /usr/bin/killall motion
sudo ps -ef | grep motion | awk '{print $2}' | xargs kill
#echo "Stop Motion!"

