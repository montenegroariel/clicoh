# Generated by Django 3.2.3 on 2021-05-29 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetail',
            name='cuantity',
            field=models.IntegerField(),
        ),
    ]
