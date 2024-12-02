# Generated by Django 5.1.3 on 2024-12-02 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_category_ar_num_remove_category_carnumber_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='area',
            field=models.CharField(choices=[('20CY', '20CY'), ('21MY', '21MY'), ('CT1', 'CT1'), ('CT2', 'CT2'), ('CT3', 'CT3'), ('CT4', 'CT4'), ('OT', 'OT'), ('PNT', 'PNT'), ('PZT', 'PZT')], max_length=5),
        ),
        migrations.AlterField(
            model_name='category',
            name='self_resolve_for_car',
            field=models.CharField(choices=[('FOR CAR', 'FOR CAR'), ('SELF RESOLVE', 'SELF RESOLVE')], max_length=12),
        ),
        migrations.AlterField(
            model_name='category',
            name='status',
            field=models.CharField(choices=[('OPEN', 'OPEN'), ('FOR CREATION', 'FOR CREATION')], max_length=12),
        ),
    ]
