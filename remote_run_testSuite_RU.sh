#!/bin/bash

# create a dated directory name for the logfile
LOGDIRECTORY=/home/nper/Desktop/Test_reults/results-`date +%Y-%m-%d-%H:%M:%S`

# execute the suite
cd /home/nper/squish/bin
./squishrunner --host 192.168.1.162 --testsuite /home/nper/Desktop/Squish_tests/suite_Geodesy_Ru/ --reportgen html,$LOGDIRECTORY

echo "


Testing is over!


"
