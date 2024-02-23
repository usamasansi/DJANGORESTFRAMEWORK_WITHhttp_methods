# Generated by Django 5.0.2 on 2024-02-23 13:54

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_todo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created_at',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('75218a59-d474-4617-8b87-f63709ba4014'), editable=False, primary_key=True, serialize=False),
        ),
    ]