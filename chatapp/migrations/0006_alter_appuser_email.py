# Generated by Django 5.1 on 2024-08-31 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0005_remove_chat_bot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='email',
            field=models.CharField(blank=True, max_length=255, unique=True),
        ),
    ]
