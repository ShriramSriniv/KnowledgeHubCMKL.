# Generated by Django 5.0.6 on 2024-05-16 07:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_training_video_pdf_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='training_video',
            name='Tools_ID01',
        ),
        migrations.DeleteModel(
            name='Tools',
        ),
        migrations.DeleteModel(
            name='Training_video',
        ),
    ]
