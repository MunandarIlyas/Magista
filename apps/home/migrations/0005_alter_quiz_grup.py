# Generated by Django 3.2.6 on 2024-04-17 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_quiz_grup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='grup',
            field=models.CharField(max_length=100),
        ),
    ]