#!/bin/bash
n=0
while true 
do	
	nohup python3 Infoavax.py &
	nohup python3 Infobsc.py &
	nohup python3 Infoftm.py &
	nohup python3 Infoeth.py &
	while ((n!=3600))
	do
		sleep 1
		((n+=1))
	done
	n=0
        for i in $(ps ax | grep Infoavax.py | grep -v grep | awk '{ print $1 }')
	do
        	kill $i
        	echo "killer avax"
	done
	for i in $(ps ax | grep Infobsc.py | grep -v grep | awk '{ print $1 }')
	do
        	kill $i
        	echo "killer bsc"
	done
	for i in $(ps ax | grep Infoftm.py | grep -v grep | awk '{ print $1 }')
	do
        	kill $i
	        echo "killer ftm"
	done
	for i in $(ps ax | grep Infoeth.py | grep -v grep | awk '{ print $1 }')
	do
	        kill $i
	        echo "killer eth"
	done


	
	echo "restart"
done
