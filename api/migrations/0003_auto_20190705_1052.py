# Generated by Django 2.2.1 on 2019-07-05 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20190705_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='odd1',
            field=models.IntegerField(help_text='Home odd'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='odd2',
            field=models.IntegerField(help_text='Draw odd'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='odd3',
            field=models.IntegerField(help_text='Away odd'),
        ),
    ]