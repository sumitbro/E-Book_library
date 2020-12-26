# Generated by Django 3.0.5 on 2020-12-20 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lib', '0007_item_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=100)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('item', models.ManyToManyField(blank=True, null=True, to='lib.Item')),
            ],
        ),
    ]
