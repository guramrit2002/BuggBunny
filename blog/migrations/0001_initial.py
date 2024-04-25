# Generated by Django 5.0.4 on 2024-04-16 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=200)),
                ('body', models.CharField(max_length=10000)),
                ('category', models.CharField(max_length=500)),
            ],
        ),
    ]
