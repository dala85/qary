# Generated by Django 3.0.5 on 2020-05-08 05:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('qary_app', '0005_auto_20200507_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 8, 5, 58, 48, 14804, tzinfo=utc)),
        ),
    ]