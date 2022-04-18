# Generated by Django 3.1.7 on 2021-06-11 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0004_vendormodel_sent_request'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendormodel',
            name='banner',
            field=models.ImageField(blank=True, default='manufacturer/default_banner.png', null=True, upload_to='vendor/profile/banner/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='vendormodel',
            name='avatar',
            field=models.ImageField(blank=True, default='manufacturer/default_ava.png', null=True, upload_to='vendor/profile/avatar/%Y/%m/%d'),
        ),
    ]