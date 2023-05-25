# Generated by Django 4.2.1 on 2023-05-25 22:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("firesale", "0013_alter_bid_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="item",
            name="member",
        ),
        migrations.AddField(
            model_name="item",
            name="user",
            field=models.ForeignKey(
                default=2,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
    ]
