# Generated by Django 4.2.6 on 2023-11-08 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file_api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='keyword',
            name='file',
        ),
        migrations.AddField(
            model_name='file',
            name='keyword',
            field=models.ManyToManyField(to='file_api.keyword'),
        ),
    ]