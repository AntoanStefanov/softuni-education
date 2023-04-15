# Generated by Django 4.0 on 2021-12-30 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('image_url', models.URLField()),
                ('description', models.TextField()),
                ('ingredients', models.CharField(max_length=255)),
                ('time', models.IntegerField()),
            ],
        ),
    ]