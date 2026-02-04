from django.apps import AppConfig
from django.contrib.auth import get_user_model
import os

class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

    def ready(self):
        if os.environ.get("CREATE_SUPERUSER") == "True":
            User = get_user_model()
            email = "hishu3851@gmail.com"
            password = "StrongPassword123"

            if not User.objects.filter(email=email).exists():
                User.objects.create_superuser(
                    email=email,
                    password=password
                )
                print("✅ Superuser created")
            else:
                print("ℹ️ Superuser already exists")
