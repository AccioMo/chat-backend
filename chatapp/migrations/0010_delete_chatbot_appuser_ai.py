# Generated by Django 5.1 on 2024-08-31 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0009_chatbot_is_public_chatbot_picture_alter_chat_topic_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ChatBot',
        ),
        migrations.AddField(
            model_name='appuser',
            name='ai',
            field=models.BooleanField(default=False),
        ),
    ]
