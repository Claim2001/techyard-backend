# Generated by Django 3.1.7 on 2021-06-07 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0025_auto_20210607_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manufacturermodel',
            name='banner2',
            field=models.ImageField(blank=True, null=True, upload_to='manufacturer/landing/avatar/%Y/%m/%d'),
        ),
    ]
