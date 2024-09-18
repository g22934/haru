# Generated by Django 5.0.6 on 2024-08-09 06:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('overview', models.TextField()),
                ('image', models.ImageField(upload_to='title_images/')),
            ],
        ),
        migrations.CreateModel(
            name='PilgrimageLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=300)),
                ('image', models.ImageField(upload_to='location_images/')),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pilgrimage.title')),
            ],
        ),
    ]
