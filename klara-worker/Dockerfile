FROM ubuntu:16.04
MAINTAINER csandoval

# Install the packages needed to run Klara
RUN apt-get update
RUN apt-get -y install python-virtualenv libmysqlclient-dev python-dev python-pip git wget
RUN apt-get -y install autoconf libtool
RUN apt-get install -y libjansson-dev
RUN apt-get install -y libmagic-dev 

# Install yara
RUN wget https://github.com/VirusTotal/yara/archive/v3.7.1.tar.gz
RUN tar xvfz v3.7.1.tar.gz
WORKDIR yara-3.7.1
RUN ./bootstrap.sh
RUN ./configure --prefix=/opt/yara-3.7.1 --enable-cuckoo --enable-magic --enable-address-sanitizer --enable-dotnet
RUN make -j4
RUN make install
RUN rm -Rf yara-3.7.1

# Create a symlink to the latest Yara version
WORKDIR /opt/
RUN ln -s yara-3.7.1/ yara-latest

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

# Install python dependencies
RUN ./.virtualenvs/klara/bin/pip install -r ./klara-github-repo/install/requirements.txt

# Copy Worker's files
RUN cp -R ./klara-github-repo/worker /var/projects/klara/worker/
COPY ./config.py /var/projects/klara/worker/config.py
RUN chown -R projects:projects /var/projects/klara/worker/

# Add exec permission to klara-worker
RUN chmod u+x /var/projects/klara/worker/klara-worker

#Install/Config Supervisor
RUN apt-get install supervisor -y
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf 

#Entrypoint
COPY entrypoint.sh /entrypoint.sh 
RUN chmod +x /entrypoint.sh
