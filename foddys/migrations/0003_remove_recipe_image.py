# Generated by Django 3.1.7 on 2021-03-21 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foddys', '0002_auto_20210321_1424'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='image',
        ),
    ]
