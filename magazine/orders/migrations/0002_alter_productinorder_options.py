# Generated by Django 4.1.7 on 2023-04-12 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productinorder',
            options={'verbose_name': 'Товары в заказе', 'verbose_name_plural': 'Товары в заказе'},
        ),
    ]
