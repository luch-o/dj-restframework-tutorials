# Generated by Django 3.2.6 on 2021-08-22 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0002_rename_snipped_snippet'),
    ]

    operations = [
        migrations.RenameField(
            model_name='snippet',
            old_name='languages',
            new_name='language',
        ),
    ]