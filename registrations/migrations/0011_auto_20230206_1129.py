# Generated by Django 3.2 on 2023-02-06 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0010_alter_childdedication_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='childdedication',
            name='created',
        ),
        migrations.AddField(
            model_name='childdedication',
            name='date_of_dedication',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='birthnotification',
            name='delivery_date',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
