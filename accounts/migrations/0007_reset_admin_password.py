from django.db import migrations
from django.contrib.auth.hashers import make_password

def reset_admin_password(apps, schema_editor):
    User = apps.get_model('accounts', 'Account')

    email = "hishu3851@gmail.com"
    password = "TempAdmin@123"

    try:
        user = User.objects.get(email=email)
        user.password = make_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.save()
    except User.DoesNotExist:
        pass


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_userprofile_profile_picture'),
    ]

    operations = [
        migrations.RunPython(reset_admin_password),
    ]
