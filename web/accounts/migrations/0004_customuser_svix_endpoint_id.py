# Generated by Django 5.1.1 on 2024-11-20 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_customuser_svix_application_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='svix_endpoint_id',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
