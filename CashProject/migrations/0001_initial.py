# Generated by Django 3.0.2 on 2020-01-28 17:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('who', models.CharField(max_length=100)),
                ('whom', models.CharField(max_length=100)),
                ('how', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CashProject.Currency')),
            ],
        ),
    ]