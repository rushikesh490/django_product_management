# Generated by Django 4.0.3 on 2022-03-08 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='type',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
