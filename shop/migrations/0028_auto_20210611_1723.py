# Generated by Django 3.1.7 on 2021-06-11 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0027_auto_20210608_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manufacturermodel',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='manufacturer/avatar/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='manufacturermodel',
            name='banner1',
            field=models.ImageField(blank=True, null=True, upload_to='manufacturer/landing/avatar/%Y/%m/%d'),
        ),
    ]