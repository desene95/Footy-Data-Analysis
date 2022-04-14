#!/bin/bash

echo "current directory using pwd command"
 echo $(pwd)
if [ $(pwd) ==  "/Users/damianesene/Documents/Footy-Data-Analysis" ]
then
echo "correct directory $(pwd)"
git add .
echo "enter commit message"
read message
git commit -m "$message"
else
echo "you are in the wrong directory, you are in  $(pwd)"
fi

