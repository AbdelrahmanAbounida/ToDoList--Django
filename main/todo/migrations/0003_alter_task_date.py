# Generated by Django 3.2.12 on 2022-04-16 02:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_alter_task_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]