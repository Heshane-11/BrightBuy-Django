from django.db import migrations

def create_admin(apps, schema_editor):
    User = apps.get_model('accounts', 'Account')
    email = "hishu3851@gmail.com"

    if not User.objects.filter(email=email).exists():
        user = User.objects.create_superuser(
            email=email,
            password="TempAdmin@123"
        )
        user.is_staff = True
        user.is_superuser = True
        user.save()

class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_userprofile_profile_picture'),
    ]

    operations = [
        migrations.RunPython(create_admin),
    ]
