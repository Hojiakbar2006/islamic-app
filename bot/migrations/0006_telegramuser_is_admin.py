# Generated by Django 5.0.2 on 2024-02-27 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0005_basicprayer_alter_ramadancalendar_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='telegramuser',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
    ]