# Generated by Django 3.1.7 on 2021-04-26 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foddys', '0015_auto_20210426_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='recipe',
            field=models.TextField(max_length=2200),
        ),
    ]
