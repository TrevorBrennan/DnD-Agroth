# Generated by Django 2.0.1 on 2019-09-28 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0004_auto_20180629_2348'),
    ]

    operations = [
        migrations.AddField(
            model_name='permissions',
            name='name',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
