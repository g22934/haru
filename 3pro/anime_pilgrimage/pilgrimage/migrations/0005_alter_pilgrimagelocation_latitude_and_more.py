# Generated by Django 5.0.6 on 2024-08-10 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pilgrimage', '0004_alter_pilgrimagelocation_latitude_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pilgrimagelocation',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pilgrimagelocation',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
