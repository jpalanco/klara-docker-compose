FROM php:5.6-fpm
MAINTAINER jpalanco


ARG MYSQL_DATABASE=klara
ARG MYSQL_USER=klara
ARG MYSQL_PASSWORD=changeme
ARG BASE_URL=http://klara.jpalanco.com
ARG WEB_ENC_KEY=FChxzdqBYBK5dvmT4hSVqtuhLmKW5tZJ
ARG KLARA_REV=4b8130511edb7e4e179dbb5c47d83a6498cefec0

# Install the packages needed to run Klara
RUN apt-get update 
RUN apt-get install -y git
RUN apt-get install -y libfreetype6-dev libjpeg62-turbo-dev libmcrypt-dev libpng-dev
RUN apt-get install -y mariadb-client 
RUN docker-php-ext-install -j$(nproc) iconv mcrypt mysqli
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/
RUN docker-php-ext-install -j$(nproc) gd

# Create an user which will be responsible
RUN groupadd -g 500 projects
RUN useradd -m -u 500 -g projects projects -d /home/projects -s /bin/bash

# Change to user projects home directory
WORKDIR /home/projects/

# Clone the repository
RUN git clone https://github.com/KasperskyLab/klara.git ./klara-github-repo
RUN chown -R projects:projects ./klara-github-repo
WORKDIR ./klara-github-repo
#RUN git checkout 4b8130511edb7e4e179dbb5c47d83a6498cefec0
RUN git checkout ${KLARA_REV}
WORKDIR ..

# Copy web files
RUN cp -R ./klara-github-repo/web /

# Copy web config files
WORKDIR /
RUN cp ./web/application/config/config.sample.php ./web/application/config/config.php
RUN cp ./web/application/config/database.sample.php ./web/application/config/database.php
RUN cp ./web/application/config/project_settings.sample.php ./web/application/config/project_settings.php
RUN sed -i -e "s@'hostname' => 'localhost'@'hostname' => 'klara-db'@" ./web/application/config/database.php 
RUN sed -i -e "s@'database' => ''@'database' => '${MYSQL_DATABASE}'@" ./web/application/config/database.php 
RUN sed -i -e "s@'username' => 'root'@'username' => '${MYSQL_USER}'@" ./web/application/config/database.php 
RUN sed -i -e "s@'password' => ''@'password' => '${MYSQL_PASSWORD}'@" ./web/application/config/database.php 
RUN sed -i -e "s@config\['base_url'\] = ''@config\['base_url'\] = '${BASE_URL}'@" ./web/application/config/config.php 
RUN sed -i -e "s@config\['encryption_key'\] = ''@config\['encryption_key'\] = '${WEB_ENC_KEY}'@" ./web/application/config/config.php 
RUN chown -R www-data:www-data ./web

# Create PHP session directory
RUN mkdir -p /var/lib/php/session
RUN chmod -R 777 /var/lib/php/session

# Update php.ini
COPY php.ini /usr/local/etc/php/

#Entrypoint
COPY entrypoint.sh /entrypoint.sh 
RUN chmod +x /entrypoint.sh

