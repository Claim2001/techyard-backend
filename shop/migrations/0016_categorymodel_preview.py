# Generated by Django 3.1.7 on 2021-04-26 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_auto_20210415_0900'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorymodel',
            name='preview',
            field=models.ImageField(blank=True, null=True, upload_to='categories/previews'),
        ),
    ]
