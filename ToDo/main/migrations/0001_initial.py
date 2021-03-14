# Generated by Django 3.0.8 on 2021-03-13 12:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('content', models.TextField(max_length=1024, verbose_name='Содержание')),
                ('time', models.DateField(default=django.utils.timezone.now, verbose_name='Дата создания')),
            ],
        ),
    ]
