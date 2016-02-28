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
divider=1000
while true 
do
   for (( i_ms=10; i_ms<1300; i_ms=2*i_ms)) # values in ms
   do
     #echo "i_ms: $i_ms"
     i_s=$(echo "scale=2; $i_ms / $divider" | bc -l)
     gpio write 7 1
     echo "LED ON"
     echo "i_s: $i_s" 
     sleep $i_s
     gpio write 7 0
     echo "LED OFF"
     sleep $i_s
   done
done
