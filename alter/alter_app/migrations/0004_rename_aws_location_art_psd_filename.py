# Generated by Django 3.2.4 on 2021-06-25 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alter_app', '0003_auto_20210622_1513'),
    ]

    operations = [
        migrations.RenameField(
            model_name='art',
            old_name='aws_location',
            new_name='psd_filename',
        ),
    ]
