# Generated by Django 3.0.3 on 2020-03-23 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='baslik',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
