# Generated by Django 4.1.4 on 2023-04-27 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Requirments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('number', models.IntegerField(max_length=10)),
                ('bookname', models.CharField(max_length=100)),
                ('edition', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.ImageField(upload_to='images'),
        ),
    ]