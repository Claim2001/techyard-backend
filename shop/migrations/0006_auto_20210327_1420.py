# Generated by Django 3.1.7 on 2021-03-27 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20210316_1203'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productmodel',
            name='properties',
        ),
        migrations.AddField(
            model_name='productmodel',
            name='characteristics',
            field=models.TextField(default='kek'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productmodel',
            name='star_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='star_total',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='image',
            field=models.ImageField(upload_to='products/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='manufacturer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='products', to='shop.manufacturermodel'),
        ),
        migrations.CreateModel(
            name='ProductTypeModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.CharField(max_length=200, unique=True)),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='product_types', to='shop.subcategorymodel')),
            ],
            options={
                'verbose_name': 'product type',
                'verbose_name_plural': 'product types',
            },
        ),
        migrations.AddField(
            model_name='productmodel',
            name='product_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='products', to='shop.producttypemodel'),
        ),
    ]
