# Generated by Django 5.1.6 on 2025-04-23 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0002_rename_release_data_album_release_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stuff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('desc', models.CharField(max_length=257)),
                ('photo', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
