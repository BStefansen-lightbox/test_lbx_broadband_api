# Generated by Django 4.1.9 on 2023-05-24 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_foobar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Foo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foo', models.IntegerField(default=0)),
            ],
        ),
        migrations.RenameModel(
            old_name='Foobar',
            new_name='Bar',
        ),
        migrations.RenameField(
            model_name='bar',
            old_name='foo',
            new_name='bar',
        ),
    ]
