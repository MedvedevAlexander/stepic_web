#! /bin/bash

#обновляем только django хотя бы до версии 2.0, остальное не трогаем. Степ 2.1 таким образом был успешно сдан.
#как же ужасен этот терминал

# Устанавливаем более свежую версию Django
sudo pip3 install django==2.0

# Копируем конфигурацию nginx
sudo cp ~/stepic_web/nginx.conf /etc/nginx/nginx.conf

# Копируем директорию проекта
sudo cp -R ~/stepic_web/web ~/web

# Запускаем nginx
sudo /etc/init.d/nginx start
sudo nginx -s reload

# wsgi файл, использующийся в одном из заданий. В дальнейшем в проекте не применяется
#cp ~/stepic_web/hello.py ~/web/hello.py

# создание БД в MySQL
sudo /etc/init.d/mysql start
sudo mysql -u root -e 'create database ask'
sudo mysql -u root -e 'create user "django"@"localhost" identified by "367UhzGhjNhfLtd*"'
sudo mysql -u root -e 'grant all privileges on ask.* to "django"@"localhost"'

# Создание таблиц в Django
cd ~web/ask
python3 manage.py makemigrations
python3 manage.py migrate

# Запуск backend сервера (для получения запросов по WSGI)
cd ~/web/ask
sudo gunicorn -b 0.0.0.0:8000 ask.wsgi:application
