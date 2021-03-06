# Generated by Django 3.2.4 on 2021-06-19 22:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=255)),
                ('birthday', models.DateField()),
                ('color', models.CharField(max_length=255)),
                ('sport', models.CharField(max_length=255)),
                ('movie', models.CharField(max_length=255)),
                ('music', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to='login_app.user')),
                ('liked_by', models.ManyToManyField(related_name='user_matches', to='login_app.User')),
            ],
        ),
    ]
