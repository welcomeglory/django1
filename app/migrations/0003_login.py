# Generated by Django 4.2.15 on 2024-08-19 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_member'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
