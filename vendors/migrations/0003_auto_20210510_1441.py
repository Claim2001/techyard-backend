# Generated by Django 3.1.7 on 2021-05-10 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0002_auto_20210510_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendormodel',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='vendor/profile'),
        ),
    ]
