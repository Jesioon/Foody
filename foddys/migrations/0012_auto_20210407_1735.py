# Generated by Django 3.1.7 on 2021-04-07 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foddys', '0011_recipe_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(blank=True, default='defaultRecipex640.jpg', upload_to=''),
        ),
    ]