# Generated by Django 4.2.1 on 2023-05-11 04:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizz', '0004_alter_test_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='end_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2023, 5, 18, 4, 9, 29, 316170, tzinfo=datetime.timezone.utc)),
        ),
    ]
