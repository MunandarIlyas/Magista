# Generated by Django 3.2.6 on 2024-04-21 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_quiz_grup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kelas',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
