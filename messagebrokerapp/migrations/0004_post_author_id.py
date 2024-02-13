# Generated by Django 4.2.6 on 2024-02-13 17:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('messagebrokerapp', '0003_alter_user_is_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
