# Generated by Django 3.2.6 on 2021-08-26 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_item_item_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_img',
            field=models.CharField(default='https://s3.amazonaws.com/ODNUploads/563be68403b50placeholder_food_item_2.png', max_length=500),
        ),
    ]
