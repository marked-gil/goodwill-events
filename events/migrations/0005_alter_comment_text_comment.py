# Generated by Django 3.2.16 on 2022-11-19 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='text_comment',
            field=models.TextField(max_length=250),
        ),
    ]