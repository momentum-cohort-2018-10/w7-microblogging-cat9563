# Generated by Django 2.1.4 on 2018-12-15 02:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20181214_1834'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='body',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='description',
        ),
    ]