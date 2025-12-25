from django.db import migrations

def reset_admin(apps, schema_editor):
    User = apps.get_model('accounts', 'Account')
    email = "hishu3851@gmail.com"
    password = "TempAdmin@123"

    try:
        user = User.objects.get(email=email)
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.save()
    except User.DoesNotExist:
        user = User.objects.create_superuser(
            email=email,
            password=password
        )

class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_create_admin'),  # update if number differs
    ]

    operations = [
        migrations.RunPython(reset_admin),
    ]
