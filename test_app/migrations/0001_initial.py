# Generated by Django 4.2.7 on 2023-11-17 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_code', models.TextField()),
                ('description', models.CharField(max_length=120)),
            ],
        ),
    ]
