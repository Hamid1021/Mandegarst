# Generated by Django 5.1.4 on 2024-12-10 22:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_alter_game_options_alter_game_game_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='application.game', verbose_name='بازی'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='position',
            field=models.CharField(choices=[('t', 'بالا'), ('m', 'وسط'), ('b', 'پایین')], max_length=1, verbose_name='موقعیت'),
        ),
    ]
