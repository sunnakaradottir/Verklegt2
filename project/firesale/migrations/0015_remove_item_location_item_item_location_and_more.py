# Generated by Django 4.1.6 on 2023-05-26 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firesale', '0014_remove_item_member_item_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='location',
        ),
        migrations.AddField(
            model_name='item',
            name='item_location',
            field=models.CharField(default='Reykjavik', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(default='Item for sale', max_length=100),
            preserve_default=False,
        ),
    ]