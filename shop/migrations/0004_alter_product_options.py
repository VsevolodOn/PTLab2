# Generated by Django 3.2.9 on 2021-12-03 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_purchase_count'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('name',)},
        ),
    ]
