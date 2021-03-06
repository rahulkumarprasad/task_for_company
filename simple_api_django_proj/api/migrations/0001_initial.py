# Generated by Django 3.2.12 on 2022-02-26 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaskModel',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Checked', models.BooleanField()),
                ('Name', models.CharField(max_length=400)),
                ('Type', models.CharField(max_length=400)),
                ('Age', models.BigIntegerField()),
                ('Description', models.CharField(max_length=400)),
                ('Date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
