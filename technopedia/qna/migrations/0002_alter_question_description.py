# Generated by Django 4.0.2 on 2022-03-12 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qna', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='description',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
