#! /bin/bash

#обновляем только django хотя бы до версии 2.0, остальное не трогаем. Степ 2.1 таким образом был успешно сдан.
#как же ужасен этот терминал

# Перед запуском на тестовом сервере необходимо:
# 1. удалить из setting.py пару ключ - значение:
#  'DIRS': [os.path.join(BASE_DIR, 'templates')],
# Из-за старой версии Django на сервере возникает ошибка
# 2. Закомментировать в web/ask/ask/__ini__.py следующие строки:
#  import pymysql
#  pymysql.install_as_MySQLdb()

# Устанавливаем более свежую версию Django
sudo pip3 install django==2.0

# Устанавливаем зависимости
sudo pip install pathlib

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
#sudo /etc/init.d/mysql start
#sudo mysql -u root -e 'create database ask'
#sudo mysql -u root -e 'create user "django"@"localhost" identified by "367UhzGhjNhfLtd*"'
#sudo mysql -u root -e 'grant all privileges on ask.* to "django"@"localhost"'

# Создание таблиц в Django
#cd ~/web/ask
#sudo python3 manage.py makemigrations
#sudo python3 manage.py migrate

# Запуск backend сервера (для получения запросов по WSGI)
cd ~/web/ask
sudo python3 gunicorn -b 0.0.0.0:8000 ask.wsgi:application
