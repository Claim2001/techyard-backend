# Generated by Django 3.1.7 on 2021-04-12 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_productmodel_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='rate',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
