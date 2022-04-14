# Generated by Django 4.0.4 on 2022-04-14 23:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('pictures', models.ImageField(upload_to='images')),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.place')),
            ],
        ),
    ]
