# Generated by Django 4.2.7 on 2023-11-16 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_user_is_staff_user_is_superadmin_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_admin',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_superadmin',
        ),
    ]