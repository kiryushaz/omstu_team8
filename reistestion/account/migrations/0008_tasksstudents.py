# Generated by Django 3.2.2 on 2021-05-10 05:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_groupssubjects_lessonstasks_modulethemes_subjectsmodules_subjectsteachers_themeslessons'),
    ]

    operations = [
        migrations.CreateModel(
            name='TasksStudents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Mark', models.IntegerField(verbose_name='Оценка')),
                ('Student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Students_key')),
                ('Task', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='account.tasksnames', verbose_name='Task_key')),
            ],
        ),
    ]
