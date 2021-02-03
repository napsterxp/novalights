#!/bin/bash
echo 'Running from device startup' > /var/www/html/webstatus.txt
cd /home/pi/Documents
python novalights.py
