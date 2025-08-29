from django.contrib.auth import get_user_model

User = get_user_model()

username = "admin"
email = "admin@example.com"
password = "admin"

if not User.objects.filter(username=username).exists():
    print("Creating superuser...")
    User.objects.create(username=username, email=email, password=password,is_superuser=True)
else:
    print("Superuser already exists.")
