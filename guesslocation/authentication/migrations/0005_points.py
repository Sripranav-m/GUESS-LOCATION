# Generated by Django 3.0.3 on 2020-02-28 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_guess'),
    ]

    operations = [
        migrations.CreateModel(
            name='points',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=100)),
                ('point', models.IntegerField(default=0)),
            ],
        ),
    ]
