# Generated by Django 5.0.1 on 2024-03-15 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seminar2_app', '0003_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='product_photos/'),
        ),
    ]
