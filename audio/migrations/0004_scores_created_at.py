# Generated by Django 2.1 on 2018-09-23 05:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0003_scores'),
    ]

    operations = [
        migrations.AddField(
            model_name='scores',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
