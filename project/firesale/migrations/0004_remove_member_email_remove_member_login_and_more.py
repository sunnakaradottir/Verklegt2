# Generated by Django 4.2.1 on 2023-05-22 11:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("firesale", "0003_alter_bid_id_alter_category_id_alter_image_id_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="member",
            name="email",
        ),
        migrations.RemoveField(
            model_name="member",
            name="login",
        ),
        migrations.AlterField(
            model_name="item",
            name="bid_id",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="firesale.bid",
            ),
        ),
        migrations.AlterField(
            model_name="item",
            name="category_id",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="firesale.category",
            ),
        ),
        migrations.AlterField(
            model_name="item",
            name="description",
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name="item",
            name="image_id",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="firesale.image",
            ),
        ),
        migrations.AlterField(
            model_name="item",
            name="location_id",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="firesale.location",
            ),
        ),
        migrations.AlterField(
            model_name="item",
            name="price",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="member",
            name="bio",
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name="member",
            name="image_id",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="firesale.image",
            ),
        ),
        migrations.AlterField(
            model_name="review",
            name="comment",
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.DeleteModel(
            name="LogIn",
        ),
    ]
