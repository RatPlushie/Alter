# Generated by Django 3.2.4 on 2021-06-22 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alter_app', '0002_auto_20210619_1345'),
    ]

    operations = [
        migrations.AddField(
            model_name='art',
            name='description',
            field=models.TextField(default='lorem ipsum'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='art',
            name='title',
            field=models.CharField(default='lorem ipsum', max_length=200),
            preserve_default=False,
        ),
    ]
