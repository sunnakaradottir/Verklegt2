# Generated by Django 4.2.1 on 2023-06-01 22:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0005_notificationsettings"),
    ]

    operations = [
        migrations.AddField(
            model_name="notificationsettings",
            name="email_address",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
