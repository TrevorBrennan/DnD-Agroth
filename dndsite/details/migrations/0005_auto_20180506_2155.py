# Generated by Django 2.0.1 on 2018-05-07 01:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0004_auto_20180506_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='source',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='details', to='details.Source', db_index=False),
        ),
        migrations.AlterField(
            model_name='tag',
            name='source',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='details', to='details.Source'),
        ),
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail_text', models.TextField()),
                ('source', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='details', to='details.Source')),
            ],
        ),
        migrations.AlterField(
            model_name='tag',
            name='source',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tags', to='details.Source'),
        ),
        migrations.AddField(
            model_name='detail',
            name='tags',
            field=models.ManyToManyField(to='details.Tag'),
        ),
    ]
