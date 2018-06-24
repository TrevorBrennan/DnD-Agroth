# Generated by Django 2.0.1 on 2018-06-24 21:04

from django.db import migrations


def populate_permissions_for_details_app(apps, schema_editor):
    Permissions = apps.get_model('authorization', 'Permissions')
    Detail = apps.get_model('details', 'Detail')
    Chapter = apps.get_model('details', 'Chapter')
    Source = apps.get_model('details', 'Source')

    permissions_qs = Permissions.objects.filter(gm_only=True, authorized_characters=None)
    if len(permissions_qs) == 0:
        permission = Permissions()
        permission.save()
    else:
        permission = permissions_qs[0]

    for detail in Detail.objects.all():
        if detail.permissions is None:
            detail.permissions = permission
            detail.save()

    for chapter in Chapter.objects.all():
        if chapter.permissions is None:
            chapter.permissions = permission
            chapter.save()

    for source in Source.objects.all():
        if source.permissions is None:
            source.permissions = permission
            source.save()


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0008_auto_20180624_1645'),
        ('authorization', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_permissions_for_details_app),
    ]
