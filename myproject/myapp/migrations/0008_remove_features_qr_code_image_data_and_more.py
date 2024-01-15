# Generated by Django 4.2.2 on 2023-11-03 16:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0007_remove_features_qr_code_image_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="features",
            name="qr_code_image_data",
        ),
        migrations.AddField(
            model_name="features",
            name="qr_code_image",
            field=models.ImageField(blank=True, upload_to="qr_codes"),
        ),
    ]
