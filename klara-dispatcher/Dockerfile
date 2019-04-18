FROM ubuntu:16.04
MAINTAINER jpalanco 

ARG KLARA_REV=4b8130511edb7e4e179dbb5c47d83a6498cefec0

# Install the packages needed to run Dispatcher
RUN apt-get update
RUN apt-get -y install python-virtualenv libmysqlclient-dev python-dev python-pip git

# Create an user which will be responsible to run Worker as well as Dispatcher
RUN groupadd -g 500 projects
RUN useradd -m -u 500 -g projects projects -d /home/projects -s /bin/bash

# Create a folder needed to store all Klara project files
RUN mkdir -p /var/projects/
RUN mkdir -p /var/projects/klara/
RUN mkdir -p /var/projects/klara/logs/
RUN chown -R projects:projects /var/projects/

# Change to user projects home directory
WORKDIR /home/projects/

# Create the virtual-env
RUN virtualenv ./.virtualenvs/klara
RUN chown -R projects:projects ./.virtualenvs/

# Clone the repository
RUN git clone https://github.com/KasperskyLab/klara.git ./klara-github-repo
RUN chown -R projects:projects ./klara-github-repo
WORKDIR ./klara-github-repo
#RUN git checkout 4b8130511edb7e4e179dbb5c47d83a6498cefec0
RUN git checkout ${KLARA_REV} 
WORKDIR ..

# Install python dependencies
RUN ./.virtualenvs/klara/bin/pip install -r ./klara-github-repo/install/requirements.txt

# Copy Dispatcher's files
RUN cp -R ./klara-github-repo/dispatcher /var/projects/klara/dispatcher/
COPY ./config.py /var/projects/klara/dispatcher/config.py
RUN chown -R projects:projects /var/projects/klara/dispatcher/

# Add exec permission to klara-dispatcher
RUN chmod u+x /var/projects/klara/dispatcher/klara-dispatcher

# Install mysqlclient
RUN apt-get install mysql-client -y

#Install/Config Supervisor
RUN apt-get install supervisor -y
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf 

#Entrypoint
COPY entrypoint.sh /entrypoint.sh 
RUN chmod +x /entrypoint.sh
