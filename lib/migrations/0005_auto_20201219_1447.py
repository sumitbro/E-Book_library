# Generated by Django 3.0.5 on 2020-12-19 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lib', '0004_auto_20201219_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='img',
            field=models.ImageField(upload_to='pics'),
        ),
    ]
