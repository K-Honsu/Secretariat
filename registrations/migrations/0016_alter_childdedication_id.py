# Generated by Django 4.1 on 2023-02-18 01:11

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0015_alter_childdedication_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='childdedication',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True),
        ),
    ]
