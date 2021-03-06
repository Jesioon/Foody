# Generated by Django 3.1.7 on 2021-03-21 13:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_name', models.CharField(max_length=50)),
                ('publication_date', models.DateTimeField(auto_now_add=True)),
                ('time_need', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(600)])),
                ('image', models.ImageField(height_field=440, upload_to='uploads/', width_field=800)),
                ('ingredients', models.CharField(max_length=400)),
                ('recipe', models.CharField(max_length=1000)),
                ('likes', models.IntegerField(verbose_name=django.core.validators.MinValueValidator(0))),
            ],
        ),
    ]
