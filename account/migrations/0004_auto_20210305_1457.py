# Generated by Django 3.1.7 on 2021-03-05 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20210226_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemodel',
            name='gender',
            field=models.CharField(blank=True, choices=[('woman', 'Woman'), ('man', 'Man')], max_length=10, null=True),
        ),
    ]
