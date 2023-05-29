# Generated by Django 4.2.1 on 2023-05-27 20:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0002_profile_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="bio",
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name="profile",
            name="favorite_item",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="favorite_item",
                to="firesale.item",
            ),
        ),
    ]