# Generated by Django 2.0.3 on 2020-03-05 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0018_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='suggustedQuantity',
            field=models.IntegerField(null=True),
        ),
    ]
