
from __future__ import unicode_literals
from django.db import migrations
from django.contrib.auth.admin import User

def create_superuser(apps, schema_editor):
    superuser = User()
    superuser.is_active = True
    superuser.is_superuser = True
    superuser.is_staff = True
    superuser.username = 'akosovski'
    superuser.email = 'akhtacaesar@gmail.com'
    superuser.set_password('Ussiowabb61')
    superuser.save()

class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.RunPython(create_superuser)
    ]