#!/bin/sh

# Once Dispatcher and Web Interfaces are set-up and configured to point to DB, the SQL DB needs to be created
if [ ! -f '/var/lib/mysql/klara/users.ibd' ]; then
	(sleep 60; mysql -uklara -p128200O_o -Dklara < /opt/klara/db-patches/db_schema.sql)&
fi

/docker-entrypoint.sh mysqld
