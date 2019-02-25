FROM php:5.6-fpm
MAINTAINER csandoval

# Install the packages needed to run Klara
RUN apt-get update 
RUN apt-get install -y git
RUN apt-get install -y libfreetype6-dev libjpeg62-turbo-dev libmcrypt-dev libpng-dev
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

# Copy web files
RUN cp -R ./klara-github-repo/web /

# Copy web config files
WORKDIR /
ADD conf/config.php ./web/application/config/config.php
ADD conf/database.php ./web/application/config/database.php
ADD conf/project_settings.php ./web/application/config/project_settings.php
RUN chown -R www-data:www-data ./web

# Create PHP session directory
RUN mkdir -p /var/lib/php/session
RUN chmod -R 777 /var/lib/php/session

# Update php.ini
COPY php.ini /usr/local/etc/php/

#Entrypoint
COPY entrypoint.sh /entrypoint.sh 
RUN chmod +x /entrypoint.sh

