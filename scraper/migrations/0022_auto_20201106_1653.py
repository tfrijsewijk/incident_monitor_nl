# Generated by Django 3.0.5 on 2020-11-06 15:53

from django.db import migrations, models
import uuid

def gen_uuid(apps, schema_editor):
    MyModel = apps.get_model('scraper', 'Incidents')
    for row in MyModel.objects.all():
        row.uuid = uuid.uuid4()
        row.save()


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0021_auto_20201106_1653'),
    ]

    operations = [
        migrations.RunPython(gen_uuid, reverse_code=migrations.RunPython.noop),
    ]
