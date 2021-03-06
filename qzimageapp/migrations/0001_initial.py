# Generated by Django 3.1.3 on 2022-02-18 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QkAttr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qzid', models.CharField(blank=True, max_length=255, null=True)),
                ('class1', models.CharField(blank=True, max_length=255, null=True)),
                ('class2', models.CharField(blank=True, max_length=255, null=True)),
                ('filepath', models.CharField(blank=True, max_length=255, null=True)),
                ('time', models.CharField(blank=True, max_length=255, null=True)),
                ('author', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.CharField(blank=True, max_length=625, null=True)),
            ],
            options={
                'db_table': 'qk_attr',
                'managed': False,
            },
        ),
    ]
