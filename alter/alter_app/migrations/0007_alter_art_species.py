# Generated by Django 3.2.4 on 2021-07-04 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alter_app', '0006_alter_art_species'),
    ]

    operations = [
        migrations.AlterField(
            model_name='art',
            name='species',
            field=models.CharField(max_length=200),
        ),
    ]
