# Generated by Django 3.2.9 on 2021-12-02 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('Todo', 'Todo'), ('Done', 'Done')], default='Todo', max_length=10),
        ),
    ]