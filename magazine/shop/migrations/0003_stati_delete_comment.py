# Generated by Django 4.1.7 on 2023-06-20 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stati',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фотография')),
                ('title', models.CharField(max_length=60)),
                ('content', models.TextField(blank=True, verbose_name='Статья')),
            ],
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
