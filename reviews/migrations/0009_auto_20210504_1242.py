# Generated by Django 3.1.7 on 2021-05-04 07:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0008_auto_20210503_1723'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviewmodel',
            name='image_1',
        ),
        migrations.RemoveField(
            model_name='reviewmodel',
            name='image_2',
        ),
        migrations.RemoveField(
            model_name='reviewmodel',
            name='image_3',
        ),
        migrations.RemoveField(
            model_name='reviewmodel',
            name='image_4',
        ),
        migrations.CreateModel(
            name='ReviewImageModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.reviewmodel')),
            ],
        ),
    ]
