# Generated by Django 4.1.2 on 2022-11-19 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kanban',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('Status', models.CharField(max_length=100)),
                ('Priority', models.CharField(blank=True, max_length=100, null=True)),
                ('Summary', models.CharField(blank=True, max_length=100, null=True)),
                ('Type', models.CharField(blank=True, max_length=100, null=True)),
                ('Tags', models.CharField(blank=True, max_length=100, null=True)),
                ('Assignee', models.CharField(blank=True, max_length=100, null=True)),
                ('Color', models.CharField(blank=True, max_length=100, null=True)),
                ('ClassName', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]