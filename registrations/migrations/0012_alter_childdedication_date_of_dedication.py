# Generated by Django 3.2 on 2023-02-06 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0011_auto_20230206_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='childdedication',
            name='date_of_dedication',
            field=models.CharField(auto_created=True, max_length=100, null=True),
        ),
    ]
