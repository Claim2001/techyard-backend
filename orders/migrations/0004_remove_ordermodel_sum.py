# Generated by Django 3.1.7 on 2021-04-14 08:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_ordermodel_sum'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordermodel',
            name='sum',
        ),
    ]