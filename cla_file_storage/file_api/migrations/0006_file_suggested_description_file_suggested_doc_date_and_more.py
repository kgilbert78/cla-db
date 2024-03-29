# Generated by Django 4.2.6 on 2024-03-09 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file_api', '0005_file_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='suggested_description',
            field=models.TextField(default='none - testing'),
        ),
        migrations.AddField(
            model_name='file',
            name='suggested_doc_date',
            field=models.DateField(default='2024-03-09'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='file',
            name='suggested_doc_date_range_end',
            field=models.DateField(default='2024-03-09'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='file',
            name='suggested_keyword',
            field=models.CharField(default="['n/a']", max_length=200),
        ),
        migrations.AddField(
            model_name='file',
            name='suggested_name',
            field=models.CharField(default='none suggested', max_length=150),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='file',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
