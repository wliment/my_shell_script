#!/bin/bash
a=`amulecmd -c status | grep ">"`
notify-send "amule" "$a" -i /home/wliment/图片/icon/amule.png -u critical

