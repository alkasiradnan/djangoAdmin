# Generated by Django 2.2.5 on 2020-01-02 05:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('writer_definition', '0001_initial'),
        ('transformer_definition', '0001_initial'),
        ('reader_definition', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Configuration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('configurationName', models.CharField(max_length=50)),
                ('reader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reader_definition.ReaderDefinition')),
                ('transformer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transformer_definition.TransformerDefinition')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='writer_definition.WriterDefinition')),
            ],
        ),
    ]