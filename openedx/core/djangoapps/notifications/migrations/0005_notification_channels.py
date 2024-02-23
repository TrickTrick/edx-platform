# Generated by Django 4.2.10 on 2024-02-22 18:08

from django.db import migrations, models
import openedx.core.djangoapps.notifications.models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0004_auto_20230607_0757'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='channels',
            field=models.JSONField(null=True, validators=[openedx.core.djangoapps.notifications.models.validate_channels]),
        ),
    ]
