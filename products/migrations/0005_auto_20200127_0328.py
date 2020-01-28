# Generated by Django 3.0.2 on 2020-01-27 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_featured'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='featured',
            new_name='featured_row_1',
        ),
        migrations.AddField(
            model_name='product',
            name='featured_row_2',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='featured_row_3',
            field=models.BooleanField(default=False),
        ),
    ]