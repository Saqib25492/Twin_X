# Generated by Django 4.2.4 on 2023-08-03 16:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_book', '0005_likepost_alter_post_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likepost',
            name='post_id',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 3, 21, 36, 2, 869138)),
        ),
    ]
