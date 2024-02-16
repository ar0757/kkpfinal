# Generated by Django 3.2.19 on 2024-02-14 03:26

from django.db import migrations, models
import shortuuid.main


class Migration(migrations.Migration):

    dependencies = [
        ('volunteers', '0021_alter_volunteer_profiles_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteer_profiles',
            name='id',
            field=models.CharField(default=shortuuid.main.ShortUUID.uuid, editable=False, max_length=22, primary_key=True, serialize=False),
        ),
    ]