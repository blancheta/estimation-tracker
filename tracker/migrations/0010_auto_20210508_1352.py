# Generated by Django 3.1.7 on 2021-05-08 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0009_auto_20210409_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='correctness',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='estimateb_by_calc',
            field=models.CharField(default='00:00', max_length=253, null=True),
        ),
    ]
