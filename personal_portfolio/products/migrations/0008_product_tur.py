# Generated by Django 3.0.3 on 2020-03-20 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20200320_1726'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='tur',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]