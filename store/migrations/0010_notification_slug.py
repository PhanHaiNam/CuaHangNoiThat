# Generated by Django 3.2.3 on 2021-12-20 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_comment_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='slug',
            field=models.TextField(default='DEFAULT VALUE'),
        ),
    ]