# Generated by Django 4.2.6 on 2023-11-08 18:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0021_remove_rentedhotel_days_rentedhotel_check_out_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rentedhotel',
            old_name='Check_out',
            new_name='check_out',
        ),
    ]
