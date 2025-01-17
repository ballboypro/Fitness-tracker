# Generated by Django 5.1.3 on 2024-11-05 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_customuser_born_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='gender',
            field=models.CharField(choices=[('female', 'FEMALE'), ('male', 'MALE')], max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='height',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='weight',
            field=models.FloatField(null=True),
        ),
    ]
