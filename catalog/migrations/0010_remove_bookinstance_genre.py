# Generated by Django 2.1.3 on 2018-11-05 01:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_auto_20181105_0830'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookinstance',
            name='genre',
        ),
    ]