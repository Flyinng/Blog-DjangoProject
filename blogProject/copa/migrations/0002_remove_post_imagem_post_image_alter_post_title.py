# Generated by Django 4.1 on 2022-09-23 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('copa', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='imagem',
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]