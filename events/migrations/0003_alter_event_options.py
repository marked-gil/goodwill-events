# Generated by Django 3.2.16 on 2022-10-17 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20221017_0030'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['-event_date']},
        ),
    ]
