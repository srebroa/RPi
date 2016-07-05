#!/bin/bash
#sudo /etc/init.d/motion start
echo "Start Motion!"
motion -n -c /home/pi/motion/motion.conf 1>/dev/null 2>&1 </dev/null &

