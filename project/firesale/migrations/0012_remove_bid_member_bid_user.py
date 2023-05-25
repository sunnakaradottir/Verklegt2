# Generated by Django 4.2.1 on 2023-05-25 19:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("firesale", "0011_alter_item_member"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="bid",
            name="member",
        ),
        migrations.AddField(
            model_name="bid",
            name="user",
            field=models.OneToOneField(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
    ]
