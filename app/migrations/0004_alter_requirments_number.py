# Generated by Django 4.1.4 on 2023-04-27 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_requirments_alter_product_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requirments',
            name='number',
            field=models.IntegerField(),
        ),
    ]
