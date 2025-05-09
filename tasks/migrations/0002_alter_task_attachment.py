# Generated by Django 3.2.25 on 2025-04-27 09:33

import cloudinary.models
from django.db import migrations
import tasks.validators


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='attachment',
            field=cloudinary.models.CloudinaryField(blank=True, default='default/default_image_omif5j', max_length=255, validators=[tasks.validators.validate_file_size, tasks.validators.validate_file_type], verbose_name='file'),
        ),
    ]
