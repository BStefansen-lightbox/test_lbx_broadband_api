# Generated by Django 4.1.9 on 2023-05-24 20:43

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0002_submissions_backend_qa_results_submissions_file_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='submissions',
            name='isp_name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='submissions',
            name='guid',
            field=models.UUIDField(default=uuid.UUID('be886b68-a203-4359-8f3a-613d61bc53d5')),
        ),
    ]