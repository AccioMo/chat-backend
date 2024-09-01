# Generated by Django 5.1 on 2024-08-31 14:35

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0007_alter_appuser_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatBot',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=255, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(default='', max_length=40)),
                ('description', models.TextField()),
            ],
        ),
    ]
