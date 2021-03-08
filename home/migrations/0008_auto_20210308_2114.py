# Generated by Django 3.1.4 on 2021-03-08 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20210308_2110'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='quantity_type',
        ),
        migrations.AddField(
            model_name='groceryitem',
            name='quantity_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='home.quantity'),
        ),
    ]
