# Generated by Django 3.0.2 on 2020-01-17 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20200117_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizzaprices',
            name='price',
            field=models.IntegerField(null=True),
        ),
    ]
