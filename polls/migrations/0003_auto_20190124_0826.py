# Generated by Django 2.0.2 on 2019-01-24 08:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_choices'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choices',
            old_name='question',
            new_name='poll',
        ),
        migrations.RemoveField(
            model_name='choices',
            name='vote',
        ),
    ]
