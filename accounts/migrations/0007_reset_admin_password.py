from django.db import migrations


def reset_admin_password(apps, schema_editor):
    User = apps.get_model('accounts', 'Account')

    email = "hishu3851@gmail.com"
    password = "TempAdmin@123"

    try:
        user = User.objects.get(email=email)
        user.set_password(password)  # ✅ SAFE inside migrations
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
