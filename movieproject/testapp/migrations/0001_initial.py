# Generated by Django 5.0.2 on 2024-03-03 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MovieModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Release_Date', models.DateField()),
                ('Movie_name', models.CharField(max_length=30)),
                ('Hero_name', models.CharField(max_length=30)),
                ('Heroine_name', models.CharField(max_length=30)),
                ('rating', models.IntegerField()),
            ],
        ),
    ]
