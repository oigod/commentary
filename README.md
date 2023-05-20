# Commentary Project

The simple Django project for writing commentary.


## Check the project:

- [x] [Commentary](https://comentar.life/)


## Requirements:
- [x] Docker must be installed in your system.


```shell
git clone https://github.com/oigod/commentary.git
cd commentary
Create .env file in root directory and commentary_bot directory by the .env.sample. example
docker-compose up
```

## Features:
* [x] Write commentary and reply to commentary
* [x] Attach image and file to commentary
* [x] Telegram bot for receiving notifications
* [x] Some visual effects for images
* [x] Admin panel


## Makefile commands(only after `docker-compose up`):
* [x] `makemigrations` - generate db migrations
* [x] `migrate` - migrate generated migrations
* [x] `createsuperuser` - create superuser
* [x] `collectstatic` - collect static files
* [x] `appshell` - run terminal for app service in container
* [x] `dbshell` - run terminal for db service in container


## Some useful links:
* [x] [Telegram bot](https://t.me/CommentaryOIBot)
* [x] [Telegram Notification Chat](https://t.me/+JIeRgONZjpowNDMy)
