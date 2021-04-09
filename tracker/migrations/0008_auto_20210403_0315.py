# Generated by Django 3.1.7 on 2021-04-03 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0007_auto_20210227_0813'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('planning', models.TimeField()),
                ('estimate', models.TimeField()),
                ('realtime', models.TimeField()),
                ('risk', models.CharField(choices=[('-', '-'), ('Not risky', 'not risky'), ('OK', 'OK'), ('Risky', 'risky'), ('Very risky', 'very risky')], max_length=100, null=True)),
                ('level', models.CharField(choices=[('-', '-'), ('Easy', 'easy'), ('Medium', 'medium'), ('Hard', 'Hard')], max_length=100, null=True)),
                ('notes', models.CharField(max_length=253, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Table',
        ),
    ]
