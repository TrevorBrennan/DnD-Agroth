# Generated by Django 2.0.1 on 2019-02-05 04:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0004_auto_20180629_2348'),
        ('details', '0012_auto_20190203_1849'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='permissions',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='authorization.Permissions'),
        ),
    ]
