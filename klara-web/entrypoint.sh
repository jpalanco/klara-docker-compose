#!/bin/sh


# Once Dispatcher and Web Interfaces are set-up and configured to point to DB, the SQL DB needs to be created
if [ ! -f /tmp/configured ]; then
   sleep 15
   # FIXME: some commands this should be done in Dockerfile
   cd /home/projects/klara-github-repo
   echo "INSERT INTO `agents` (`id`, `description`, `auth`) VALUES (1, 'test', 'test');" >> ./install/db_patches/db_schema.sql
   mysql -u$MYSQL_USER -p$MYSQL_PASSWORD -D$MYSQL_DATABASE -h klara-db < ./install/db_patches/db_schema.sql && touch /tmp/configured && echo 'Finished';
else
  echo 'Already configured';
fi

php-fpm
