# Generated by Django 2.2.4 on 2020-08-21 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hlist', '0005_memo'),
    ]

    operations = [
        migrations.AddField(
            model_name='memo',
            name='memoid',
            field=models.IntegerField(default=1),
        ),
    ]