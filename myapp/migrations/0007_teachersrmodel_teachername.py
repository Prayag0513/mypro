# Generated by Django 4.2.11 on 2024-03-17 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_courses'),
    ]

    operations = [
        migrations.AddField(
            model_name='teachersrmodel',
            name='teacherName',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
