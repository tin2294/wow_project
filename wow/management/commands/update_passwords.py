# update_passwords.py

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


class Command(BaseCommand):
    help = 'Update passwords for existing users'

    def handle(self, *args, **options):
        users = User.objects.all()

        for user in users:
            user.set_password(user.password)  # Update the password using the existing password
            user.save()

        self.stdout.write(self.style.SUCCESS('Passwords updated successfully'))
