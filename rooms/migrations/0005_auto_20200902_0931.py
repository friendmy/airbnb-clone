# Generated by Django 2.2.5 on 2020-09-02 00:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0004_auto_20200902_0902'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='cournty',
            new_name='country',
        ),
    ]
