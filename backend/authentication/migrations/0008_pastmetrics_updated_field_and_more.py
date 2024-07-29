# Generated by Django 5.0.6 on 2024-07-29 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0007_pastmetrics'),
    ]

    operations = [
        migrations.AddField(
            model_name='pastmetrics',
            name='updated_field',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pastmetrics',
            name='blood_pressure',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='patientprofile',
            name='blood_pressure',
            field=models.TextField(blank=True, null=True),
        ),
    ]
