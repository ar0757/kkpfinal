# Generated by Django 3.2.19 on 2024-04-24 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tempstorage', '0003_alter_tempstorage_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tempstorage',
            name='data',
            field=models.JSONField(),
        ),
    ]