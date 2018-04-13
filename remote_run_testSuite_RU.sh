#!/bin/bash

# create a dated directory name for the logfile
LOGDIRECTORY=/home/Desktop/Test_reults/results-`date +%Y-%m-%d-%H:%M:%S`

# execute the suite
cd /home/squish/bin
./squishrunner --host 192.168.1.162 --testsuite /home/Desktop/Squish_tests/suite_Geodesy_Ru/ --reportgen html,$LOGDIRECTORY

echo "


Testing is over!


"
