# Generated by Django 4.2.7 on 2023-11-16 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=100, verbose_name='Sinov'),
        ),
    ]