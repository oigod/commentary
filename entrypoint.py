import os

os.system("python manage.py wait_for_db")
os.system("python manage.py migrate")
os.system("python start_bot.py > /dev/null 2>&1 &")
os.system("python manage.py runserver 0.0.0.0:8000")
