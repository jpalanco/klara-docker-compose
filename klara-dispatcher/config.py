# Setup the loglevel
logging_level  = "debug"

# What port should Dispatchers's REST API should listen to
listen_port = 8888

# Main settings for the master
# Set debug lvl
logging_level  = "debug"

# What port should the server listen to
listen_port = 8888

# Notification settings
# Do we want to sent out notification e-mails or not?
notification_email_enabled  = True
# FROM SMTP header settings
notification_email_from     = "klara-notify@example.com"
# SMTP server address
notification_email_smtp_srv = "127.0.0.1"

# MySQL / MariaDB settings for the Dispatcher to connect to the DB
mysql_host      = "klara-db"
mysql_database  = "klara"
mysql_user      = "klara"
mysql_password  = "128200O_o"

