# Generated by Django 3.0.2 on 2020-02-07 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_auto_20200203_1214'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64, null=True)),
                ('username', models.CharField(max_length=64, null=True)),
                ('password', models.CharField(max_length=64, null=True)),
            ],
        ),
    ]
