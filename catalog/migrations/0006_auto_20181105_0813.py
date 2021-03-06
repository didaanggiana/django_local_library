# Generated by Django 2.1.3 on 2018-11-05 01:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_bookinstance_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookinstance',
            name='genre',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Genre'),
        ),
        migrations.RemoveField(
            model_name='book',
            name='genre',
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Genre'),
        ),
    ]
