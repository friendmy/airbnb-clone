# Generated by Django 2.2.5 on 2020-09-16 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_user_email_secret'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='email_confirm',
            new_name='email_verified',
        ),
        migrations.AlterField(
            model_name='user',
            name='email_secret',
            field=models.CharField(default='', max_length=20),
        ),
    ]
