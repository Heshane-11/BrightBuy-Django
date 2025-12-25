from django.db import migrations

def reset_admin_password(apps, schema_editor):
    User = apps.get_model('accounts', 'Account')

    try:
        user = User.objects.get(email="hishu3851@gmail.com")
        user.set_password("TempAdmin@123")
        user.is_staff = True
        user.is_superuser = True
        user.save()
    except User.DoesNotExist:
        pass


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_create_admin'),
    ]

    operations = [
        migrations.RunPython(reset_admin_password),
    ]
