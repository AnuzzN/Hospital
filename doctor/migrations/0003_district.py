# Generated by Django 5.0.1 on 2024-02-29 09:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0002_place_alter_doctors_fname'),
    ]

    operations = [
        migrations.CreateModel(
            name='district',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50, verbose_name='District')),
                ('Place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.place')),
            ],
        ),
    ]
