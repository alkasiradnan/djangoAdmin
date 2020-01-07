# Generated by Django 2.2.5 on 2020-01-02 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ReaderDefinition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('readerName', models.CharField(max_length=50)),
                ('path', models.CharField(max_length=250)),
                ('type', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'LOCAL'), (2, 'HTTP'), (3, 'SFTP')], null=True)),
            ],
        ),
    ]
