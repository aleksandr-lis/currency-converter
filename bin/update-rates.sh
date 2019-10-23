#!/usr/bin/env bash

string=$(docker ps | grep 'app')
id=${string:0:12}

docker exec -ti $id sh -c 'python manage.py update_rates'