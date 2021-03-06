# Generated by Django 3.1.4 on 2021-03-03 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GroceryItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=500)),
                ('pub_date', models.DateField()),
                ('price', models.IntegerField(default=0)),
                ('image', models.ImageField(default='', upload_to='home/images')),
            ],
            options={
                'ordering': ('title',),
            },
        ),
    ]
