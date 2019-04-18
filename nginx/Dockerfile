FROM nginx:latest
MAINTAINER jpalanco 

ARG KLARA_REV=4b8130511edb7e4e179dbb5c47d83a6498cefec0

RUN apt-get update
RUN apt-get install -y git

WORKDIR /home/projects/
RUN git clone https://github.com/KasperskyLab/klara.git ./klara-github-repo
RUN chown -R www-data:www-data ./klara-github-repo
WORKDIR ./klara-github-repo
#RUN git checkout 4b8130511edb7e4e179dbb5c47d83a6498cefec0
RUN git checkout ${KLARA_REV}
RUN ln -s /home/projects/klara-github-repo/web /

#Entrypoint
COPY entrypoint.sh /entrypoint.sh 
RUN chmod +x /entrypoint.sh
