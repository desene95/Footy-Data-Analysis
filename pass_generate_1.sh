#!/bin/bash

#Generate password

PASS_LENGTH=16

pass=$(openssl rand -base64 48 | cut -c1-$PASS_LENGTH)
echo $pass
