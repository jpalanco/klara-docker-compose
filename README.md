# klara-docker-compose

You can learn more about klara at the original repository https://github.com/KasperskyLab/klara/ 

You can also learn mor about how to play with this repo at my blog https://www.jpalanco.com/retrohunt-for-everyone-with-klara/

Modify .env file according to your needs

Run:
`docker-compose up -d`

Wait a couple of minutes...

Connect to your instance, example: http://localhost/

## Access


For your convenience, 2 `users`, 2 `groups` and 2 `scan repositories` have been created:

* Users:

| Username      | Password                | Auth level     | Group ID     | Quota |
| ------------- |:-------------:          | :----------    | ---------    | :---- |
| admin         | `super_s3cure_password` | `16` (Admin)   | `2` (admins) | N/A (Admins don't have quuota) |
| john          | `super_s3cure_password` | `4` (Observer) | `1` (main)   | 1000 scans / month |

* Groups

| Group name    | `scan_filesets_list` (scan repositories) | Jail status |
| ------------- | :-------------                           | ----------- |
| main          | `[1,2]`                                  | 0 (OFF - Users are not jailed) |
| admins        | `[1,2]`                                  | 0 (OFF - Users are not jailed) |

* Scan Repositories (`scan_filesets` DB table)

| Scan Repository   |
| -------------     |
| /virus_repository |
| /_clean           |
