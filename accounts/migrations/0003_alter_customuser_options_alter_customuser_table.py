# Generated by Django 4.2.7 on 2023-11-16 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_customuser_delete_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={},
        ),
        migrations.AlterModelTable(
            name='customuser',
            table='user',
        ),
    ]
