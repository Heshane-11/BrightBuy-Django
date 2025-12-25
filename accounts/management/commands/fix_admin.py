from django.core.management.base import BaseCommand
from accounts.models import Account

class Command(BaseCommand):
    help = "Create or fix admin user"

    def handle(self, *args, **kwargs):
        email = "dropati5911@gmail.com"
        password = "StrongPassword123"

        user, created = Account.objects.get_or_create(
            email=email,
            defaults={
                "username": "admin",
                "first_name": "Admin",
                "last_name": "User",
            }
        )

        user.is_staff = True
        user.is_admin = True
        user.is_superadmin = True
        user.is_active = True
        user.set_password(password)
        user.save()

        if created:
            self.stdout.write(self.style.SUCCESS("✅ Superuser CREATED"))
        else:
            self.stdout.write(self.style.SUCCESS("✅ Superuser UPDATED"))
