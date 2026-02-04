import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BrightBuy.settings")
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

email = "hishu3851@gmail.com"
password = "StrongPassword123"

if not User.objects.filter(email=email).exists():
    User.objects.create_superuser(
        email=email,
        username="admin",
        first_name="Heshane",
        last_name="Garg",
        password=password
    )
    print("✅ Superuser created")
else:
    print("ℹ️ Superuser already exists")
