#!/bin/bash


while :

do

        curl http://192.168.30.29:5000/

        sleep $((RANDOM % 300 ))

done
