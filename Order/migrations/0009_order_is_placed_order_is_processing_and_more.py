# Generated by Django 5.0.7 on 2024-08-05 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0008_alter_order_items_order_alter_order_items_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='is_placed',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='is_processing',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='is_shipping',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='Is_Delivered',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
