# Generated by Django 2.0.1 on 2018-06-30 03:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0004_auto_20180629_2348'),
        ('atlas', '0003_auto_20180410_2334'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='permissions',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='authorization.Permissions'),
        ),
        migrations.AddField(
            model_name='location',
            name='prime',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='redactions', to='atlas.Location'),
        ),
        migrations.AddField(
            model_name='locationtype',
            name='permissions',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='authorization.Permissions'),
        ),
        migrations.AddField(
            model_name='locationtype',
            name='prime',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='redactions', to='atlas.LocationType'),
        ),
    ]
