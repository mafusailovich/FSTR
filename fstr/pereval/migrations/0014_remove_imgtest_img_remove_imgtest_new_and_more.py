# Generated by Django 4.1.5 on 2023-02-11 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pereval', '0013_imgtest_new_alter_imgtest_img_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imgtest',
            name='img',
        ),
        migrations.RemoveField(
            model_name='imgtest',
            name='new',
        ),
        migrations.AlterField(
            model_name='perevaladded',
            name='status',
            field=models.CharField(choices=[('2', 'pending'), ('1', 'new'), ('3', 'accepted'), ('4', 'rejected')], default='new', max_length=8),
        ),
    ]
