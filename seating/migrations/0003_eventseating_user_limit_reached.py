# Generated by Django 3.2.16 on 2022-10-31 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seating', '0002_auto_20221031_0222'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventseating',
            name='user_limit_reached',
            field=models.BooleanField(default=False),
        ),
    ]