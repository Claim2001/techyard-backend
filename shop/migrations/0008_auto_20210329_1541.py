# Generated by Django 3.1.7 on 2021-03-29 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20210329_1305'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='propertymodel',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='propertymodel',
            name='subcategory',
        ),
        migrations.RemoveField(
            model_name='productmodel',
            name='subcategory',
        ),
        migrations.AddField(
            model_name='manufacturermodel',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='manufacturers', to='shop.categorymodel'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='manufacturermodel',
            unique_together={('title', 'category')},
        ),
        migrations.DeleteModel(
            name='PropertyItemModel',
        ),
        migrations.DeleteModel(
            name='PropertyModel',
        ),
        migrations.RemoveField(
            model_name='manufacturermodel',
            name='subcategory',
        ),
    ]
