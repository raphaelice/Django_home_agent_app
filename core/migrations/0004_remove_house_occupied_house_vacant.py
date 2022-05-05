# Generated by Django 4.0.4 on 2022-04-24 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_rename_price_house_first_price_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='house',
            name='occupied',
        ),
        migrations.AddField(
            model_name='house',
            name='vacant',
            field=models.BooleanField(default=True),
        ),
    ]