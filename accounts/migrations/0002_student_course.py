# Generated by Django 2.2 on 2020-09-27 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='course',
            field=models.ManyToManyField(to='education.Course'),
        ),
    ]