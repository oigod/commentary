from django.core.management.base import BaseCommand
from django.db import connection
from django.db.utils import OperationalError
import time


class Command(BaseCommand):
    """Django command to pause execution until database is available"""

    def handle(self, *args, **kwargs):
        self.stdout.write("waiting for db ...")
        is_connected = False
        while not is_connected:
            try:
                connection.ensure_connection()
            except (OperationalError, Exception):
                self.stdout.write("Database unavailable, waiting 1 second ...")
                time.sleep(1)
            else:
                is_connected = True
                self.stdout.write(self.style.SUCCESS("db available"))
