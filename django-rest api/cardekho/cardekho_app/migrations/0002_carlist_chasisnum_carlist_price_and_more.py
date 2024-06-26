# Generated by Django 5.0.6 on 2024-06-14 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardekho_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carlist',
            name='chasisnum',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='carlist',
            name='price',
            field=models.DecimalField(decimal_places=2, default=1000, max_digits=9),
        ),
        migrations.AlterField(
            model_name='carlist',
            name='description',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
