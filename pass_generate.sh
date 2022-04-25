#!/bin/bash

#Generate password

echo "what password length do you want to have"
read PASS_LENGTH

pass=$(openssl rand -base64 48 | cut -c1-$PASS_LENGTH)
echo $pass
destdir=/Users/damianesene/Documents/Footy-Data-Analysis/password.txt
echo "$pass" > "destdir"
