# Generated by Django 4.1.5 on 2023-01-27 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pereval', '0006_alter_images_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='img',
            field=models.BinaryField(editable=True),
        ),
    ]
