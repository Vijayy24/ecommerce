# Generated by Django 4.0.5 on 2022-06-27 15:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='Customer',
            new_name='customer',
        ),
        migrations.RenameField(
            model_name='orderitem',
            old_name='qunatity',
            new_name='quantity',
        ),
    ]
