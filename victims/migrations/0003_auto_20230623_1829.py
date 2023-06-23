# Generated by Django 3.2.19 on 2023-06-23 14:29

from django.db import migrations, models
import shortuuid.main


class Migration(migrations.Migration):

    dependencies = [
        ('victims', '0002_alter_all_profiles_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='all_profiles',
            name='id',
            field=models.CharField(default=shortuuid.main.ShortUUID.uuid, editable=False, max_length=22, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='all_profiles',
            name='ngo_assigned',
            field=models.CharField(blank=True, choices=[('GodGivenHomes', 'GodGivenHomes'), ('KKGP', 'KKGP')], default='', max_length=100),
        ),
    ]