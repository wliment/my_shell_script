#!/bin/sh
 
export WAR3_PATH="/media/7e207bab-b03d-48ef-8edf-259b0d3b1436/war3/"
 
X :3 -ac -terminate &   # 在display 3上新开一个X
cd "${WAR3_PATH}"
sleep 2
DISPLAY=:3 `which wine` War3.exe -opengl #启动war3
