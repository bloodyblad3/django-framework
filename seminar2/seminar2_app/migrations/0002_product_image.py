# Generated by Django 5.0.1 on 2024-02-20 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seminar2_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='media'),
        ),
    ]
