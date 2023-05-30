# Generated by Django 4.2.1 on 2023-05-30 16:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("firesale", "0024_rename_to_member_review_to_user_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="item",
            name="image",
        ),
        migrations.RemoveField(
            model_name="itemimage",
            name="item",
        ),
        migrations.AddField(
            model_name="item",
            name="image_urls",
            field=models.ManyToManyField(to="firesale.itemimage"),
        ),
        migrations.AddField(
            model_name="item",
            name="status",
            field=models.CharField(
                choices=[("available", "Available"), ("sold", "Sold")],
                default="available",
                max_length=10,
            ),
        ),
    ]
