# Generated by Django 4.1.5 on 2023-02-07 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('super_types', '0001_initial'),
        ('supers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='super',
            name='super_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='super_types.supertype'),
            preserve_default=False,
        ),
    ]
