# Generated by Django 4.2.11 on 2024-03-15 21:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_services_image_alter_about_content'),
    ]

    operations = [
        migrations.DeleteModel(
            name='About',
        ),
    ]
