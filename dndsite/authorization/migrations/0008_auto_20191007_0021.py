# Generated by Django 2.0.1 on 2019-10-07 04:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0007_auto_20191007_0004'),
    ]

    operations = [
        migrations.RenameField(
            model_name='permissions',
            old_name='authorized_characters',
            new_name='viewers',
        ),
    ]
