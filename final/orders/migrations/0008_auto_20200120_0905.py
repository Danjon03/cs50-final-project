# Generated by Django 3.0.2 on 2020-01-20 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_auto_20200117_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizzaprices',
            name='price',
            field=models.FloatField(null=True),
        ),
    ]
