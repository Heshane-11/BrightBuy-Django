import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BrightBuy.settings")
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

email = "hishu3851@gmail.com"
password = "Admin@123"
username = "admin"
first_name = "Heshane"
last_name = "Garg"

try:
    user = User.objects.get(email=email)
    user.set_password(password)
    user.is_staff = True
    user.is_superuser = True
    user.save()
    print("✅ Superuser password RESET successfully")

except User.DoesNotExist:
    User.objects.create_superuser(
        email=email,
        username=username,
        first_name=first_name,
        last_name=last_name,
        password=password
    )
    print("✅ Superuser CREATED successfully")
