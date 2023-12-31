# Generated by Django 4.2.6 on 2023-10-22 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0006_alter_insuredfamilymember_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insuranceperson',
            name='sex',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1),
        ),
        migrations.AlterField(
            model_name='insuredfamilymember',
            name='sex',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1),
        ),
    ]
