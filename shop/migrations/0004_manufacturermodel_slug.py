# Generated by Django 3.1.7 on 2021-03-11 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20210311_1625'),
    ]

    operations = [
        migrations.AddField(
            model_name='manufacturermodel',
            name='slug',
            field=models.CharField(default=1, max_length=200, unique=True),
            preserve_default=False,
        ),
    ]