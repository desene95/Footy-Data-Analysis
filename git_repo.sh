#!/bin/bash
date_time=$(date)
Recipient="esene789@gmail.com"
Subject="New file pushed"
Message="New code pushed to your repository $date_time"

echo "current directory using pwd command"
 echo $(pwd)
if [ $(pwd) ==  "/Users/damianesene/Documents/Footy-Data-Analysis" ]
then
echo "correct directory $(pwd)"
git add .
echo "enter commit message"
read message
git commit -m "$message"
git push

`mail -s $Subject $Recipient <<< $Message`

else
echo "you are in the wrong directory, you are in  $(pwd)"
fi

