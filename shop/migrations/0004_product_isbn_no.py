# Generated by Django 2.2.1 on 2019-05-23 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20190523_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='isbn_no',
            field=models.CharField(db_index=True, default='isbn_no', max_length=50),
        ),
    ]
