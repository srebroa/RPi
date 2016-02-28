#!/bin/bash
# get wiringPi library first
<<comment
sudo apt-get update
sudo apt-get upgrade
git clone git://git.drogon.net/wiringPi
cd wiringPi
./build
comment

gpio mode 7 out # RPi GPIO4
while true; 
do
    gpio write 7 1
    echo "LED ON"
    sleep 0.5
    gpio write 7 0
    echo "LED OFF"
    sleep 0.5
done
