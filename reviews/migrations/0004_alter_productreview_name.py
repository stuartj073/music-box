# Generated by Django 3.2 on 2022-02-08 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_sku'),
        ('reviews', '0003_remove_productreview_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productreview',
            name='name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.product'),
        ),
    ]