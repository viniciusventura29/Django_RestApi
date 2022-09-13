# Generated by Django 4.0.6 on 2022-08-03 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_prod_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='prod',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photo/%y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='prod',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]