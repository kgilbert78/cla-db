# Generated by Django 4.2.6 on 2024-03-09 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file_api', '0002_file_orig_doc_date_range_end'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='upload_timestamp',
            field=models.DateTimeField(auto_now_add=True, default='2024-03-09 14:22:40.274306'),
            preserve_default=False,
        ),
    ]