# Generated by Django 5.0.4 on 2024-06-11 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LaborRegistration',
            fields=[
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('labor_id', models.CharField(blank=True, max_length=255, primary_key=True, serialize=False)),
                ('adhar_card', models.ImageField(upload_to='')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('mobile', models.CharField(max_length=255)),
                ('password', models.CharField(blank=True, max_length=255)),
                ('otp', models.CharField(blank=True, default='11111', max_length=10)),
                ('is_activate', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]