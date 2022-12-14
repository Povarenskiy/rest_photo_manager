# Generated by Django 4.1.4 on 2022-12-14 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Names',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.ImageField(blank=True, upload_to='uploads/')),
                ('date', models.DateField(blank=True, null=True)),
                ('description', models.TextField(blank=True, max_length=255)),
                ('country', models.TextField(blank=True, max_length=100)),
                ('city', models.TextField(blank=True, max_length=100)),
                ('people', models.ManyToManyField(blank=True, to='photo.names')),
            ],
        ),
    ]
