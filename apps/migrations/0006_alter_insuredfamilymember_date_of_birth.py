# Generated by Django 4.2.6 on 2023-10-22 20:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0005_rename_full_name_insuranceperson_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insuredfamilymember',
            name='date_of_birth',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]