# Generated by Django 3.1.1 on 2020-09-03 06:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='dat_posted',
            new_name='date_posted',
        ),
    ]
