# Generated by Django 4.2.5 on 2023-09-23 23:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_Messages', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='messages',
            old_name='body',
            new_name='text',
        ),
    ]