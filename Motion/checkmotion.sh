#!/bin/sh
ps -e | grep " motion" >/dev/null

if [ $? -ne 0 ]; then
   echo "motion is not running!"
   /usr/bin/sudo -u motion /usr/bin/motion >/dev/null
else
   echo "OK - motion is running"
fi
