# Generated by Django 2.1.3 on 2018-11-25 12:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20181010_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 25, 18, 18, 0, 72403)),
        ),
    ]
