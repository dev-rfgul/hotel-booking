# Generated by Django 5.2 on 2025-05-07 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base_App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='Item_name',
            field=models.CharField(max_length=40),
        ),
    ]
