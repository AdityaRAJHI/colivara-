# Generated by Django 5.1.1 on 2024-09-21 01:12

import django.contrib.postgres.fields
import django.db.models.deletion
import pgvector.django.vector
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_document'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='content',
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_number', models.IntegerField()),
                ('content', models.TextField(blank=True)),
                ('embeddings', django.contrib.postgres.fields.ArrayField(base_field=pgvector.django.vector.VectorField(dimensions=128), size=None)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pages', to='api.document')),
            ],
            options={
                'constraints': [models.UniqueConstraint(fields=('content', 'document'), name='unique_page_per_document')],
            },
        ),
    ]
