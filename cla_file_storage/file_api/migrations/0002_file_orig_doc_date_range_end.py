# Generated by Django 4.2.6 on 2024-03-08 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='orig_doc_date_range_end',
            field=models.DateField(default='2008-11-15'),
            preserve_default=False,
        ),
    ]
