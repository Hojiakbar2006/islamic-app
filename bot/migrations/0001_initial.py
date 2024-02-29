# Generated by Django 5.0.2 on 2024-02-24 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TelegramUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=255, null=True)),
                ('chat_id', models.IntegerField(unique=True)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
