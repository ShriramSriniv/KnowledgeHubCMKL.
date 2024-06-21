# Generated by Django 5.0.4 on 2024-05-13 04:48

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_customuser_is_email_verified'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tools',
            fields=[
                ('Category', models.CharField(max_length=100)),
                ('tool_id', models.PositiveIntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(99999)])),
                ('name', models.CharField(max_length=100)),
                ('descriptions', models.CharField(max_length=200)),
                ('download_link', models.URLField()),
                ('Website_link', models.URLField()),
                ('License', models.CharField(max_length=100)),
                ('Platforms', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Training_video',
            fields=[
                ('Category', models.CharField(max_length=100)),
                ('Video_id', models.PositiveIntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(99999)])),
                ('Title', models.CharField(max_length=100)),
                ('descriptions', models.CharField(max_length=200)),
                ('URL', models.URLField()),
                ('Aspect', models.URLField()),
                ('Skill_levels', models.CharField(max_length=100)),
                ('Tools_ID01', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.tools')),
            ],
        ),
    ]