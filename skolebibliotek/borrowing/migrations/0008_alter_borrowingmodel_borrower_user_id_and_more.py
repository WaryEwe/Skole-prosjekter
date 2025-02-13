# Generated by Django 5.1.4 on 2025-01-10 11:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('borrowing', '0007_remove_borrowingmodel_borrowing_id_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrowingmodel',
            name='borrower_user_id',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user_borrower', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='borrowingmodel',
            name='borrowing_image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
