# Generated by Django 4.0.4 on 2022-05-12 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0002_projectsmodel_body_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutpagemodel',
            name='body_2',
            field=models.TextField(blank=True, max_length=355, null=True),
        ),
        migrations.AddField(
            model_name='aboutpagemodel',
            name='title_2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
