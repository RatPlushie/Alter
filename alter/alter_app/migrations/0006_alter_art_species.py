# Generated by Django 3.2.4 on 2021-07-04 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alter_app', '0005_auto_20210704_0031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='art',
            name='species',
            field=models.TextField(),
        ),
    ]
