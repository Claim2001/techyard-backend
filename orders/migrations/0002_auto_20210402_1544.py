# Generated by Django 3.1.7 on 2021-04-02 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
    ]
