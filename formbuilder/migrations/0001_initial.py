# Generated by Django 5.0.4 on 2024-11-28 15:34

import django.db.models.deletion
import dynamic_forms.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('schema', dynamic_forms.models.FormField()),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response_data', dynamic_forms.models.ResponseField()),
                ('form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formbuilder.form')),
            ],
        ),
    ]
