# Generated by Django 4.2.4 on 2023-09-04 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='icon',
            field=models.CharField(default='bx-cart', max_length=100),
        ),
    ]
