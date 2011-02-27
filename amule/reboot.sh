#!/bin/bash
while [ 1 ]
do
	process_num=`ps aux |grep "amuled" |grep -v "grep" |wc -l`
	if [ $process_num -eq 1 ]; then
		echo " amule is runing at" `date` >> ./amule.log
		sleep 30
	else
		/usr/bin/amuled -f
		echo "amule dead at"`date` >> ./amule.log
	fi
done
