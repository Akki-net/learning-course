# Generated by Django 5.0.1 on 2024-01-25 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_learning', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('div_name', models.CharField(max_length=25)),
            ],
        ),
    ]
