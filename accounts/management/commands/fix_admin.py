from django.core.management.base import BaseCommand
from accounts.models import Account

class Command(BaseCommand):
    help = "Create admin user if not exists"

    def handle(self, *args, **kwargs):
        email = "dropati5911@gmail.com"
        password = "StrongPassword123"

        # ✅ EARLY EXIT IF ADMIN EXISTS
        if Account.objects.filter(email=email).exists():
            self.stdout.write(self.style.WARNING("⚠️ Superuser already exists"))
            return

        # ✅ CREATE ADMIN
        user = Account.objects.create_user(
            email=email,
            username="admin",
            first_name="Admin",
            last_name="User",
            password=password,
        )

        user.is_staff = True
        user.is_admin = True
        user.is_superadmin = True
        user.is_active = True
        user.save()

        self.stdout.write(self.style.SUCCESS("✅ Superuser CREATED"))
