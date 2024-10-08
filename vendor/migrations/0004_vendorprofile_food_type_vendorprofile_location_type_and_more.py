# Generated by Django 5.1.1 on 2024-10-01 16:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0003_vendorshoptype_vendorprofile_establishment_year_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='vendorprofile',
            name='food_type',
            field=models.CharField(choices=[('veg', 'Veg'), ('nonveg', 'Non-Veg'), ('all', 'All')], default='veg', max_length=50),
        ),
        migrations.AddField(
            model_name='vendorprofile',
            name='location_type',
            field=models.CharField(choices=[('permanent', 'Permanent'), ('movable', 'Movable Thela')], default='permanent', max_length=50),
        ),
        migrations.AddField(
            model_name='vendorprofile',
            name='sitting_available',
            field=models.CharField(choices=[('not available', 'Not available'), ('indoor', 'Indoor'), ('outdoor', 'Outdoor'), ('both', 'Both')], default='both', max_length=50),
        ),
        migrations.AddField(
            model_name='vendorprofile',
            name='size',
            field=models.CharField(choices=[('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')], default='small', max_length=10),
        ),
        migrations.CreateModel(
            name='VendorRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('behavior_rating', models.FloatField(default=0.0)),
                ('service_rating', models.FloatField(default=0.0)),
                ('quality_rating', models.FloatField(default=0.0)),
                ('cleanliness_rating', models.FloatField(default=0.0)),
                ('value_for_money_rating', models.FloatField(default=0.0)),
                ('overall_rating', models.FloatField(default=0.0)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('vendor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='vendor.vendorprofile')),
            ],
            options={
                'verbose_name_plural': 'Vendor Ratings',
                'db_table': 'vendor_ratings',
            },
        ),
    ]
