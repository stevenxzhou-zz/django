# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Favorites',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('AddDate', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MainProductCategory',
            fields=[
                ('MainCategoryName', models.CharField(max_length=45, serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('ProductID', models.IntegerField(max_length=10, serialize=False, primary_key=True)),
                ('ProductName', models.CharField(max_length=110)),
                ('ListPrice', models.DecimalField(max_digits=5, decimal_places=2)),
                ('CurrentPrice', models.DecimalField(max_digits=5, decimal_places=2)),
                ('ProductDescription', models.CharField(max_length=300)),
                ('AddDate', models.DateTimeField()),
                ('ExpirationDate', models.DateTimeField()),
                ('Hits', models.IntegerField(max_length=10)),
                ('Image', models.BinaryField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Stores',
            fields=[
                ('StoreName', models.CharField(max_length=45, serialize=False, primary_key=True)),
                ('StoreLink', models.CharField(max_length=110)),
                ('StoreLogo', models.BinaryField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SubProductCategory',
            fields=[
                ('SubCategoryName', models.CharField(max_length=45, serialize=False, primary_key=True)),
                ('MainCategoryName', models.ForeignKey(to='dealmoon.MainProductCategory')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('Email', models.CharField(max_length=45, serialize=False, primary_key=True)),
                ('Name', models.CharField(max_length=45)),
                ('Password', models.CharField(max_length=45)),
                ('Admin', models.BooleanField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='products',
            name='StoreName',
            field=models.ForeignKey(to='dealmoon.Stores'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='products',
            name='SubCategoryName',
            field=models.ForeignKey(to='dealmoon.SubProductCategory'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='favorites',
            name='Email',
            field=models.ForeignKey(to='dealmoon.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='favorites',
            name='ProductID',
            field=models.ForeignKey(to='dealmoon.Products'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='favorites',
            name='StoreName',
            field=models.ForeignKey(to='dealmoon.Stores'),
            preserve_default=True,
        ),
    ]
