# Generated by Django 3.2.16 on 2022-10-17 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='is_published',
        ),
        migrations.AddField(
            model_name='event',
            name='status',
            field=models.IntegerField(choices=[(0, 'Expired'), (1, 'Active'), (2, 'Draft')], default=2),
        ),
    ]
