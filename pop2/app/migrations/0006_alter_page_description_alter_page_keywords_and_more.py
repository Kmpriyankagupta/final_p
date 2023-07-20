# Generated by Django 4.2.3 on 2023-07-19 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_page_description_alter_page_keywords_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='description',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='page',
            name='keywords',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='pagename',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='page',
            name='title',
            field=models.CharField(max_length=500),
        ),
    ]