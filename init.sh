#! /bin/bash

#обновляем только django хотя бы до версии 2.0, остальное не трогаем. Степ 2.1 таким образом был успешно сдан.
#как же ужасен этот терминал

sudo pip3 install django==2.0
sudo cp ~/stepic_web/nginx.conf /etc/nginx/nginx.conf
sudo cp -R ~/stepic_web/web ~/web
sudo /etc/init.d/nginx start
sudo nginx -s reload
#cp ~/stepic_web/hello.py ~/web/hello.py
cd ~/web/ask
sudo gunicorn -b 0.0.0.0:8000 ask.wsgi:application
