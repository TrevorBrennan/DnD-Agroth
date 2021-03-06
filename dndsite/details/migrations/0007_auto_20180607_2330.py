# Generated by Django 2.0.1 on 2018-06-08 03:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0006_auto_20180519_1325'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chapters', to='details.Source')),
            ],
        ),
        migrations.AddField(
            model_name='detail',
            name='chapter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='details', to='details.Chapter'),
        ),
    ]
