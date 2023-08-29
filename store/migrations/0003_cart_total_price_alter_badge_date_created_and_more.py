# Generated by Django 4.2.4 on 2023-08-29 17:48

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_images_image_alter_badge_date_created_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='total_price',
            field=models.CharField(default='0', max_length=244, null=True),
        ),
        migrations.AlterField(
            model_name='badge',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 29, 22, 48, 21, 342098), null=True),
        ),
        migrations.AlterField(
            model_name='badge',
            name='title',
            field=models.CharField(blank=True, max_length=244, null=True),
        ),
        migrations.AlterField(
            model_name='cart',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 29, 22, 48, 21, 342098), null=True),
        ),
        migrations.AlterField(
            model_name='cartproduct',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 29, 22, 48, 21, 342098), null=True),
        ),
        migrations.AlterField(
            model_name='cartproduct',
            name='price',
            field=models.CharField(blank=True, max_length=244, null=True),
        ),
        migrations.AlterField(
            model_name='cartproduct',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.product'),
        ),
        migrations.AlterField(
            model_name='cartproduct',
            name='quantity',
            field=models.CharField(blank=True, max_length=244, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 29, 22, 48, 21, 342098), null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(blank=True, max_length=244, null=True),
        ),
        migrations.AlterField(
            model_name='frequentlyaskedquestions',
            name='answer',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='frequentlyaskedquestions',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 29, 22, 48, 21, 342098), null=True),
        ),
        migrations.AlterField(
            model_name='frequentlyaskedquestions',
            name='question',
            field=models.CharField(blank=True, max_length=244, null=True),
        ),
        migrations.AlterField(
            model_name='images',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 29, 22, 48, 21, 342098), null=True),
        ),
        migrations.AlterField(
            model_name='images',
            name='title',
            field=models.CharField(blank=True, max_length=244, null=True),
        ),
        migrations.AlterField(
            model_name='listfield',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 29, 22, 48, 21, 342098), null=True),
        ),
        migrations.AlterField(
            model_name='listfield',
            name='title',
            field=models.CharField(blank=True, max_length=244, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='cart',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.cart'),
        ),
        migrations.AlterField(
            model_name='order',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 29, 22, 48, 21, 342098), null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery_status',
            field=models.CharField(blank=True, choices=[('pending', 'pending'), ('shipped', 'shipped'), ('delivered', 'delivered'), ('declined', 'declined'), ('canceled', 'canceled'), ('returned', 'returned')], max_length=244, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_type',
            field=models.CharField(blank=True, choices=[('card', 'card'), ('payoneer', 'patoneer'), ('ethereum', 'ethereum')], max_length=244, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='city',
            field=models.CharField(blank=True, max_length=244, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='coins',
            field=models.CharField(blank=True, default='0', max_length=244),
        ),
        migrations.AlterField(
            model_name='person',
            name='country',
            field=models.CharField(blank=True, default='Pakistan', max_length=244),
        ),
        migrations.AlterField(
            model_name='person',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 29, 22, 48, 21, 342098), null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='first_name',
            field=models.CharField(blank=True, max_length=244, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='last_name',
            field=models.CharField(blank=True, max_length=244, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='role',
            field=models.CharField(blank=True, choices=[('customer', 'customer'), ('member', 'member')], default='customer', max_length=244),
        ),
        migrations.AlterField(
            model_name='person',
            name='street',
            field=models.CharField(blank=True, max_length=244, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='Badge',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.badge'),
        ),
        migrations.AlterField(
            model_name='product',
            name='commision',
            field=models.CharField(blank=True, max_length=244, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 29, 22, 48, 21, 342098), null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='employee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.person'),
        ),
        migrations.AlterField(
            model_name='product',
            name='old_price',
            field=models.CharField(blank=True, max_length=244, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.CharField(blank=True, max_length=244, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='shipping_price',
            field=models.CharField(blank=True, max_length=244, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(blank=True, max_length=244, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='total_price',
            field=models.CharField(blank=True, max_length=244, null=True),
        ),
    ]
