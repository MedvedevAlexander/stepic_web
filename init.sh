#! /bin/bash

sudo cp ~/stepic_web/nginx.conf /etc/nginx/nginx.conf
sudo /etc/init.d/nginx start
sudo nginx -s reload
mkdir -p ~/web/public/img
mkdir ~/web/public/css
mkdir ~/web/public/js
mkdir ~/web/uploads
mkdir ~/web/etc
cp ~/stepic_web/hello.py ~/web/hello.py
