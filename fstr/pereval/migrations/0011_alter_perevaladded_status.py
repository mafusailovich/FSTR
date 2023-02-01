# Generated by Django 4.1.5 on 2023-01-31 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pereval', '0010_alter_perevaladded_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perevaladded',
            name='status',
            field=models.CharField(choices=[('3', 'accepted'), ('1', 'new'), ('2', 'pending'), ('4', 'rejected')], default='new', max_length=8),
        ),
    ]
