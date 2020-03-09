# Generated by Django 2.0.3 on 2020-02-27 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0013_auto_20200218_1014'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemName', models.CharField(max_length=64, null=True)),
                ('quantity', models.IntegerField(null=True)),
                ('productCode', models.IntegerField(null=True)),
                ('productPrice', models.IntegerField(null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Ingredients',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='PizzaPrices',
        ),
    ]