# Generated by Django 5.1.4 on 2025-01-13 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('borrowing', '0017_alter_borrowingmodel_borrowing_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrowingmodel',
            name='borrowing_image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
