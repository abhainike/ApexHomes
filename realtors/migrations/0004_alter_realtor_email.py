# Generated by Django 4.2.6 on 2023-11-06 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0003_alter_realtor_email_alter_realtor_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='email',
            field=models.CharField(max_length=50),
        ),
    ]
