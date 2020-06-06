# Generated by Django 2.2.10 on 2020-03-20 15:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('borrowers', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='borrower',
            name='admin_creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_borrowers', to=settings.AUTH_USER_MODEL),
        ),
    ]