# Generated by Django 2.2.4 on 2020-10-06 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hlist', '0011_remove_memo_memoid'),
    ]

    operations = [
        migrations.CreateModel(
            name='fileupload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('milname', models.CharField(max_length=10)),
                ('milfile', models.ImageField(upload_to='mil')),
            ],
        ),
    ]