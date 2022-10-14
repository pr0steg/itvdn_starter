# Generated by Django 4.1.2 on 2022-10-13 15:28

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('lesson_5', '0002_alter_bouquet_fresh_period_alter_bouquet_price_and_more'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='bouquet',
            managers=[
                ('shop', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='client',
            name='discount_size',
            field=models.DecimalField(decimal_places=5, max_digits=5, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='invoice',
            field=models.FileField(null=True, upload_to='uploads/%Y/%m/%d/'),
        ),
    ]
