import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

username = "admin"
email = "admin@example.com"
password = "adminpassword"

if not User.objects.filter(username=username).exists():
    print("Creating superuser...")
    User.objects.create(username=username, email=email, password=password,is_superuser=True)
else:
    print("Superuser already exists.")
