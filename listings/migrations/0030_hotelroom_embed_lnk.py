# Generated by Django 4.2.3 on 2023-11-12 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0029_rentedhotel_reviewdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotelroom',
            name='embed_lnk',
            field=models.TextField(null=True),
        ),
    ]
