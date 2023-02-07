# Generated by Django 4.1.3 on 2023-02-06 17:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_task_diskr'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'verbose_name': 'Задача', 'verbose_name_plural': 'Задачи'},
        ),
        migrations.AddField(
            model_name='task',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата события'),
            preserve_default=False,
        ),
    ]