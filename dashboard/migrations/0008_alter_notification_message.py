# Generated by Django 5.0.6 on 2024-06-12 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_notification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='message',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
