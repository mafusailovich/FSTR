# Generated by Django 4.1.5 on 2023-01-30 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pereval', '0008_perevaladded_status_alter_perevaladded_level_autumn_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perevaladded',
            name='status',
            field=models.CharField(choices=[('4', 'rejected'), ('2', 'pending'), ('1', 'new'), ('3', 'accepted')], default='new', max_length=8),
        ),
        migrations.AlterField(
            model_name='perevaladded',
            name='title',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
