# Generated by Django 3.1.7 on 2021-05-27 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0018_auto_20210527_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='year',
            field=models.DateTimeField(),
        ),
    ]
