# Generated by Django 3.2.3 on 2022-01-14 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0019_lastseen_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(max_length=150, verbose_name='Quận/Huyện'),
        ),
        migrations.AlterField(
            model_name='address',
            name='state',
            field=models.CharField(max_length=150, verbose_name='Thành Phố/Tỉnh'),
        ),
    ]
