#!/bin/bash
set -m

cmd="mongod --httpinterface --rest --master --auth"
 
$cmd &
 
if [ ! -f /data/db/.mongodb_password_set ]; then
    /set_mongodb_password.sh
fi

fg
