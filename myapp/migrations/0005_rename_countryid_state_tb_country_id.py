# Generated by Django 4.2.6 on 2023-10-17 08:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_state_tb'),
    ]

    operations = [
        migrations.RenameField(
            model_name='state_tb',
            old_name='Countryid',
            new_name='Country_id',
        ),
    ]