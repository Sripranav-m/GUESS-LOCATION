# Generated by Django 3.0.3 on 2020-02-26 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_auto_20200226_1448'),
    ]

    operations = [
        migrations.CreateModel(
            name='guess',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=100)),
                ('guess', models.CharField(default='', max_length=100)),
                ('num', models.IntegerField()),
            ],
        ),
    ]
