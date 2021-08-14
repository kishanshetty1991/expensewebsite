# Generated by Django 3.2.6 on 2021-08-14 14:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterField(
            model_name='expense',
            name='date',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
