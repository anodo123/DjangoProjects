# Generated by Django 4.2.6 on 2024-02-12 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messagebrokerapp', '0002_alter_user_subscribers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_author',
            field=models.BooleanField(default=False),
        ),
    ]