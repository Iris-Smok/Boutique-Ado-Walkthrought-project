# Generated by Django 3.2 on 2022-06-20 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_auto_20220620_1335'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='grand_bag',
            new_name='original_bag',
        ),
    ]
