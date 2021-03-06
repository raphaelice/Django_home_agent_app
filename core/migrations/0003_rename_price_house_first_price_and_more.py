# Generated by Django 4.0.4 on 2022-04-24 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_images_image_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='house',
            old_name='price',
            new_name='first_price',
        ),
        migrations.AddField(
            model_name='house',
            name='subsequent_price',
            field=models.PositiveIntegerField(default=140000),
            preserve_default=False,
        ),
    ]
