# Generated by Django 5.1.4 on 2025-01-13 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('borrowing', '0012_remove_borrowingmodel_borrowing_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrowingmodel',
            name='borrowing_image',
            field=models.ImageField(default=1, upload_to='images/'),
        ),
    ]