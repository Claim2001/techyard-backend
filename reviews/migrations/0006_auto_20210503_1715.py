# Generated by Django 3.1.7 on 2021-05-03 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0005_auto_20210503_1713'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reviewmodel',
            old_name='image',
            new_name='image_1',
        ),
        migrations.AddField(
            model_name='reviewmodel',
            name='image_2',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='reviewmodel',
            name='image_3',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='reviewmodel',
            name='image_4',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
