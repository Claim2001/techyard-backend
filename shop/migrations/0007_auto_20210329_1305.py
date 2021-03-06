# Generated by Django 3.1.7 on 2021-03-29 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20210327_1420'),
    ]

    operations = [
        migrations.CreateModel(
            name='LandingModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner1', models.ImageField(blank=True, null=True, upload_to='landing/1')),
                ('banner2', models.ImageField(blank=True, null=True, upload_to='landing/2')),
                ('banner3', models.ImageField(blank=True, null=True, upload_to='landing/3')),
            ],
            options={
                'verbose_name': 'landing banner',
                'verbose_name_plural': 'landing banners',
            },
        ),
        migrations.AddField(
            model_name='categorymodel',
            name='banner1',
            field=models.ImageField(blank=True, null=True, upload_to='categories'),
        ),
        migrations.AddField(
            model_name='categorymodel',
            name='banner2',
            field=models.ImageField(blank=True, null=True, upload_to='categories'),
        ),
    ]
