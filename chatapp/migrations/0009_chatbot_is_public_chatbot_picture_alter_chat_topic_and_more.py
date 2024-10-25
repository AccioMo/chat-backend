# Generated by Django 5.1 on 2024-08-31 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0008_chatbot'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatbot',
            name='is_public',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='chatbot',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='chatbot_pics/'),
        ),
        migrations.AlterField(
            model_name='chat',
            name='topic',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='chatbot',
            name='name',
            field=models.CharField(default='unknown-bot', max_length=40),
        ),
    ]