#!/bin/bash
userfile=/Users/damianesene/Documents/Footy-Data-Analysis/userlist
username=$(cat /Users/damianesene/Documents/Footy-Data-Analysis/userlist)
password=$(./pass_generate_1.sh)
for user in $username
do
sudo su -
dscl . create /Users/ $user
echo $password | passwd --stdin $user
done
echo "$(wc -l /Users/damianesene/Documents/Footy-Data-Analysis/userlist) users have been created"
tail -n$(wc -l /Users/damianesene/Documents/Footy-Data-Analysis/userlist) /etc/passwd

