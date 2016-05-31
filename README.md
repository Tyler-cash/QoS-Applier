# QoS-Applier
This script updates the QoS settings on a DD-WRT router. The download and upload speeds are measured by using the speedtest_cli library.

# Reason for script
I use QoS to ensure my games don't lag and to prioritize video streaming over general webpage traffic. The problem is my download speed
fluctuates wildly due to congestion on my ISP's end of the pipe. I needed something that would automatically update my DD-WRT router's
QoS download speed because it was becoming incredibly tedious to do manually. Now I have this script to do it for me. It generally takes
about 30 seconds to run and will update my download speed at the click of a button rather than 6 whole buttons! Wow, savings!

# How to use?
Set the username variable to be whatever your username is on your router. Also make a python module that contains a variable with your
router's password contained inside of it. Then simply let the script run and it will set the download speed to your current download speed.
Now in windows scheduler run this script every 30 minutes and your speed will be automatically updated every 30 minutes.

By uncommenting the upload speed, lines of code it's possible to autonomously update the upload speed as well. But currently the library
has a bug with python 3.5 so it has been commented out until it's corrected.

# Changes made to speedtest_cli
The library's speedtest function now exits slightly prematurely and returns both the upload and download speeds.
