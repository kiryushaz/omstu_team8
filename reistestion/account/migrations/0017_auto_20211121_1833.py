# Generated by Django 3.2.2 on 2021-11-21 12:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0016_auto_20211121_1819'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='groupssubjects',
            options={'verbose_name': 'Связь: Предмет - Группа', 'verbose_name_plural': 'Связь: Предмет - Группа'},
        ),
        migrations.AlterModelOptions(
            name='lessonstasks',
            options={'verbose_name': 'Связь: Тема - Задание', 'verbose_name_plural': 'Связь: Тема - Задание'},
        ),
        migrations.AlterModelOptions(
            name='modulethemes',
            options={'verbose_name': 'Связь: Тема - Модуль', 'verbose_name_plural': 'Связь: Тема - Модуль'},
        ),
        migrations.AlterModelOptions(
            name='subjectsteachers',
            options={'verbose_name': 'Связь: Предмет - Педагог', 'verbose_name_plural': 'Связь: Предмет - Педагог'},
        ),
        migrations.AlterModelOptions(
            name='tasksstudents',
            options={'verbose_name': 'Связь: Студент - Задание', 'verbose_name_plural': 'Связь: Студент - Задание'},
        ),
        migrations.AlterModelOptions(
            name='themeslessons',
            options={'verbose_name': 'Связь: Тема - Занятие', 'verbose_name_plural': 'Связь: Тема - Занятие'},
        ),
        migrations.AlterField(
            model_name='groupssubjects',
            name='Group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.groupnames', verbose_name='Group_key'),
        ),
        migrations.AlterField(
            model_name='groupssubjects',
            name='Subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.subjectsnames', verbose_name='Subject_key'),
        ),
        migrations.AlterField(
            model_name='lessonstasks',
            name='Lesson',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.lessonsnames', verbose_name='Lessons_key'),
        ),
        migrations.AlterField(
            model_name='lessonstasks',
            name='Task',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.tasksnames', verbose_name='Task_key'),
        ),
        migrations.AlterField(
            model_name='modulethemes',
            name='Model',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.modulesnames', verbose_name='Module_key'),
        ),
        migrations.AlterField(
            model_name='modulethemes',
            name='Theme',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.themesnames', verbose_name='Theme_key'),
        ),
        migrations.AlterField(
            model_name='subjectsteachers',
            name='Subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.subjectsnames', verbose_name='Subject_key'),
        ),
        migrations.AlterField(
            model_name='subjectsteachers',
            name='Teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Teacher_key'),
        ),
        migrations.AlterField(
            model_name='tasksstudents',
            name='Student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Students_key'),
        ),
        migrations.AlterField(
            model_name='tasksstudents',
            name='Task',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.tasksnames', verbose_name='Task_key'),
        ),
        migrations.AlterField(
            model_name='themeslessons',
            name='Lesson',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.lessonsnames', verbose_name='Lessons_key'),
        ),
        migrations.AlterField(
            model_name='themeslessons',
            name='Theme',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.themesnames', verbose_name='Theme_key'),
        ),
    ]
