# Generated by Django 4.1.5 on 2023-01-30 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pereval', '0009_alter_perevaladded_status_alter_perevaladded_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perevaladded',
            name='status',
            field=models.CharField(choices=[('4', 'rejected'), ('3', 'accepted'), ('1', 'new'), ('2', 'pending')], default='new', max_length=8),
        ),
    ]
