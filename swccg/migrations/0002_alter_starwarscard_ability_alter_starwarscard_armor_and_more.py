# Generated by Django 4.1.3 on 2022-11-22 15:34

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swccg', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='starwarscard',
            name='ability',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='starwarscard',
            name='armor',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='starwarscard',
            name='characteristics',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='starwarscard',
            name='conceptBy',
            field=models.TextField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='starwarscard',
            name='destiny',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='starwarscard',
            name='errataVersion',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='starwarscard',
            name='extraText',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, default='', max_length=200), size=None),
        ),
        migrations.AlterField(
            model_name='starwarscard',
            name='forfeit',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='starwarscard',
            name='gametext',
            field=models.TextField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='starwarscard',
            name='gempId',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='starwarscard',
            name='hyperspeed',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='starwarscard',
            name='icons',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, default='', max_length=200), size=None),
        ),
        migrations.AlterField(
            model_name='starwarscard',
            name='imageUrl',
            field=models.URLField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='starwarscard',
            name='landspeed',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='starwarscard',
            name='legacy',
            field=models.BooleanField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='starwarscard',
            name='lore',
            field=models.TextField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='starwarscard',
            name='maneuver',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='starwarscard',
            name='parsec',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='starwarscard',
            name='politics',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='starwarscard',
            name='power',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='starwarscard',
            name='rarity',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='starwarscard',
            name='set',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='starwarscard',
            name='side',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='starwarscard',
            name='sourceType',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='starwarscard',
            name='subType',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='starwarscard',
            name='title',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='starwarscard',
            name='type',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='starwarscard',
            name='uniqueness',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
    ]
