# Generated by Django 4.2.11 on 2024-03-19 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0003_alter_booking_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='service',
            field=models.CharField(choices=[('online individual therapy', 'Online Individual Therapy'), ('online family therapy', 'Online Family Therapy'), ('workshop', 'Workshop')], default='online_individual_therapy', max_length=50),
        ),
    ]