# Generated by Django 4.2.3 on 2023-08-02 15:06

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='id',
        ),
        migrations.AddField(
            model_name='content',
            name='idContent',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
