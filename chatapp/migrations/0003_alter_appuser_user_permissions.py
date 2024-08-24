# Generated by Django 4.2.13 on 2024-06-13 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('chatapp', '0002_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, related_name='appuser_permissions', to='auth.permission'),
        ),
    ]