# Generated by Django 3.0.5 on 2020-06-04 13:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.IntegerField()),
                ('name', models.CharField(default='', max_length=300, null=True)),
                ('category', models.CharField(default='', max_length=30)),
                ('makerName', models.CharField(default='', max_length=50, null=True)),
                ('photoUrl', models.CharField(max_length=500)),
                ('createdDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('publishedDate', models.DateTimeField(null=True)),
                ('achievementRate', models.IntegerField(default=0)),
                ('totalAmount', models.IntegerField(default=0)),
                ('totalSupporter', models.IntegerField(default=0)),
                ('totalLike', models.IntegerField(default=0)),
                ('endYn', models.BooleanField(default=False)),
                ('detailUrl', models.CharField(max_length=500)),
            ],
            options={
                'ordering': ['createdDate'],
            },
        ),
    ]