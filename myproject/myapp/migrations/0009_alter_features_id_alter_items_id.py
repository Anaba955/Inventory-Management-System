# Generated by Django 4.2.2 on 2023-11-04 12:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0008_remove_features_qr_code_image_data_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="features",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="items",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
