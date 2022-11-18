# Generated by Django 4.1.2 on 2022-11-18 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Subject', models.CharField(max_length=100)),
                ('Location', models.CharField(max_length=100)),
                ('StartTime', models.DateTimeField()),
                ('EndTime', models.DateTimeField()),
                ('IsAllDay', models.BooleanField(default=False)),
                ('Status', models.CharField(max_length=100)),
                ('Priority', models.CharField(max_length=100)),
                ('CategoryColor', models.CharField(max_length=100)),
            ],
        ),
    ]