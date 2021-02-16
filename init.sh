#! /bin/bash

#sudo pip3 install django==2.0
sudo cp ~/stepic_web/nginx.conf /etc/nginx/nginx.conf
sudo cp -R ~/stepic_web/web ~/web
sudo /etc/init.d/nginx start
sudo nginx -s reload
#cp ~/stepic_web/hello.py ~/web/hello.py
