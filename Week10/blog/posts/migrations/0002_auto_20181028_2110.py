# Generated by Django 2.0.5 on 2018-10-28 15:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 28, 21, 10, 13, 386767)),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='static/images/posts'),
        ),
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 28, 21, 10, 13, 385767), null=True),
        ),
    ]
