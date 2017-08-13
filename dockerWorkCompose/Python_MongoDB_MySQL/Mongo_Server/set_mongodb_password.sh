#!/bin/bash
 
# Admin User
MONGODB_ADMIN_USER=$MONGODB_ADMIN_USER
MONGODB_ADMIN_PASS=$MONGODB_ADMIN_PASS

# Warten bis MongoDB läuft
RET=1
while [[ RET -ne 0 ]]; do
    sleep 5
    mongo admin --eval "help" >/dev/null 2>&1
    RET=$?
done
 
# Erstellen admin user
mongo admin --eval "db.createUser({user: '$MONGODB_ADMIN_USER', pwd: '$MONGODB_ADMIN_PASS', roles:[{role:'root',db:'admin'}]});"
sleep 3
 
touch /data/db/.mongodb_password_set