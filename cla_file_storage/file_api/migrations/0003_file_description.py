# Generated by Django 4.2.6 on 2023-11-08 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file_api', '0002_remove_keyword_file_file_keyword'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
