# Generated by Django 5.0.4 on 2024-05-03 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauths', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=25, null=True, unique=True),
        ),
    ]