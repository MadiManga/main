# Generated by Django 3.2.5 on 2021-11-04 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20211104_1932'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mangacart',
            old_name='img',
            new_name='cover1',
        ),
        migrations.RemoveField(
            model_name='mangacart',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='mangacart',
            name='title',
        ),
        migrations.AddField(
            model_name='mangacart',
            name='description1',
            field=models.CharField(default=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='mangacart',
            name='manga1',
            field=models.CharField(default=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='mangacart',
            name='price1',
            field=models.IntegerField(default=True, verbose_name='Цена'),
        ),
    ]
