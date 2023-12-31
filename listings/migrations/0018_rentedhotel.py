# Generated by Django 4.2.6 on 2023-11-08 17:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('listings', '0017_alter_listing_contact_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='RentedHotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listings.hotelroom')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
