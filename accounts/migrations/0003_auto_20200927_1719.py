# Generated by Django 2.2 on 2020-09-27 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_student_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='last_seen',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
