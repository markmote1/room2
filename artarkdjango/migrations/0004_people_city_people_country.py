# Generated by Django 4.2.3 on 2023-07-31 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artarkdjango', '0003_people_delete_student_delete_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='people',
            name='city',
            field=models.CharField(default='Nairobi', max_length=50),
        ),
        migrations.AddField(
            model_name='people',
            name='country',
            field=models.CharField(default='Kenya', max_length=50),
        ),
    ]
