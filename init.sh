#! /bin/bash

sudo cp ~/stepic_web/nginx.conf /etc/nginx/nginx.conf
sudo cp ~/stepic_web/web /home/box/web
sudo /etc/init.d/nginx start
sudo nginx -s reload
#cp ~/stepic_web/hello.py ~/web/hello.py
