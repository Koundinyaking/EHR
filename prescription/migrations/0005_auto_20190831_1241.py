# Generated by Django 2.2.2 on 2019-08-31 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prescription', '0004_auto_20190824_0914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prescriptions',
            name='record',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
