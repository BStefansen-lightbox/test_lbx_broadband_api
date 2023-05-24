# Generated by Django 4.1.9 on 2023-05-24 20:37

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='submissions',
            name='backend_qa_results',
            field=models.JSONField(default=dict),
        ),
        migrations.AddField(
            model_name='submissions',
            name='file_name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='submissions',
            name='guid',
            field=models.UUIDField(default=uuid.UUID('60b47665-d254-4ad9-a2b2-4a3adfa82449')),
        ),
    ]
