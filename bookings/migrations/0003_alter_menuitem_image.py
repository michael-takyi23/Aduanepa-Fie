# Generated by Django 5.0.7 on 2024-07-31 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0002_menuitem_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='image',
            field=models.ImageField(default='default_image.jpg', upload_to='images/'),
            preserve_default=False,
        ),
    ]
