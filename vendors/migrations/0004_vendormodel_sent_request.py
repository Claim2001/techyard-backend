# Generated by Django 3.1.7 on 2021-06-09 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0003_auto_20210510_1441'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendormodel',
            name='sent_request',
            field=models.BooleanField(default=False),
        ),
    ]
