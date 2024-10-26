# Generated by Django 5.1.2 on 2024-10-25 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('display', '0002_alter_game_harga'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='alamat1',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='game',
            name='alamat2',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='game',
            name='alamat3',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='game',
            name='toko1',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='game',
            name='toko2',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='game',
            name='toko3',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
