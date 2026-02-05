from django.core.management.base import BaseCommand
from accounts.models import Account

class Command(BaseCommand):
    help = "Create or reset admin user"

    def handle(self, *args, **kwargs):
        email = "hishu3851@gmail.com"
        password = "12345"   # 🔐 FINAL password

        try:
            user = Account.objects.get(email=email)

            # 🔁 RESET PASSWORD
            user.set_password(password)
            user.is_staff = True
            user.is_admin = True
            user.is_superadmin = True
            user.is_active = True
            user.save()

            self.stdout.write(
                self.style.SUCCESS("✅ Superuser EXISTS — password RESET successfully")
            )

        except Account.DoesNotExist:
            # 🆕 CREATE USER
            user = Account.objects.create_user(
                email=email,
                username="admin",
                first_name="Heshane",
                last_name="Garg",
                password=password,
            )
            user.is_staff = True
            user.is_admin = True
            user.is_superadmin = True
            user.is_active = True
            user.save()

            self.stdout.write(
                self.style.SUCCESS("✅ Superuser CREATED successfully")
            )
