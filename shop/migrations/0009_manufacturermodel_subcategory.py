# Generated by Django 3.1.7 on 2021-03-29 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_auto_20210329_1541'),
    ]

    operations = [
        migrations.AddField(
            model_name='manufacturermodel',
            name='subcategory',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='manufacturers', to='shop.subcategorymodel'),
            preserve_default=False,
        ),
    ]
