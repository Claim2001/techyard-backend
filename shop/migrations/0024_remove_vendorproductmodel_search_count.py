# Generated by Django 3.1.7 on 2021-05-31 07:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0023_auto_20210531_1132'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendorproductmodel',
            name='search_count',
        ),
    ]
