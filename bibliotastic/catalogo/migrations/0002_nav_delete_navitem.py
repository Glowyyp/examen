# Generated by Django 4.1.2 on 2024-07-12 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nav',
            fields=[
                ('id_nav', models.AutoField(db_column='idNav', primary_key=True, serialize=False)),
                ('nombre_nav', models.CharField(max_length=20)),
                ('url_nav', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'Navs',
            },
        ),
        migrations.DeleteModel(
            name='NavItem',
        ),
    ]
