# Generated by Django 5.1.1 on 2024-10-07 15:06

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_remove_queryembedding_query_delete_query_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='name',
            field=models.CharField(db_index=True, max_length=255),
        ),
        migrations.AddIndex(
            model_name='collection',
            index=models.Index(fields=['name', 'owner'], name='collection_name_owner_idx'),
        ),
    ]
