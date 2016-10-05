#!/bin/bash

# Challenge I2
# https://www.reddit.com/r/dailyprogrammer/comments/pjbuj/intermediate_challenge_2/

GHP="10"
HP="10"

while [ "$GHP" -gt "0" ];
	do
		echo "You are fighting a hostile goblin! (HP $GHP)"
		echo "What are you going to do? (HP $HP)"
		echo "1. Attack (-2 HP)"
		echo "2. Block"
		echo "3. Throw Rock (-1 HP)"

		read response

		AI=`awk -v min=0 -v max=9 -v seed=$RANDOM 'BEGIN{srand(seed); print int(min+rand()*(max-min+1))}'`
		echo $AI
		
		if [ "$AI" -gt "5" ]; then
			ai_action="block"
		else
			ai_action="attack"
		fi

		if [ "$response" == "2" ]; then
				echo "Goblin "$ai_action"ed!"
				echo "You blocked!"
		else
			echo "You attacked!"
			if [ "$ai_action" == "block" ]; then
				echo "Goblin blocked!"
			elif [ "$response" == "3" ]; then
				echo "Goblin attacked!"
				GHP=$[$GHP - 1]
				HP=$[$HP - 1]
			elif [ "$response" == "1" ]; then
				echo "Goblin attacked!"
				GHP=$[$GHP - 2]
				HP=$[$HP - 1]
			fi
		fi
	done

