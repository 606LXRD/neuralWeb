# Generated by Django 4.1.7 on 2023-07-04 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0002_alter_manualinput_age_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manualinput',
            name='num',
            field=models.IntegerField(max_length=30, null=True),
        ),
    ]
