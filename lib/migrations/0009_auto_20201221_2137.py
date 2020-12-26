# Generated by Django 3.0.5 on 2020-12-21 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lib', '0008_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='date_added',
        ),
        migrations.AddField(
            model_name='order',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
    ]