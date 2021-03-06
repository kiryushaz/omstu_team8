# Generated by Django 3.2.2 on 2021-11-21 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0014_auto_20211121_1501'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='semesterssubjects',
            options={'verbose_name': 'Связь: Предмет - Семестр', 'verbose_name_plural': 'Связь: Предмет - Семестр'},
        ),
        migrations.RemoveField(
            model_name='semesterssubjects',
            name='Semester',
        ),
        migrations.RemoveField(
            model_name='semesterssubjects',
            name='Subject',
        ),
        migrations.AddField(
            model_name='semester',
            name='subjects',
            field=models.ManyToManyField(blank=True, through='account.SemestersSubjects', to='account.SubjectsNames'),
        ),
        migrations.AddField(
            model_name='semesterssubjects',
            name='semester',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='account.semester'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='semesterssubjects',
            name='subject',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='account.subjectsnames'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='semester',
            name='Week1',
            field=models.CharField(blank=True, max_length=255, verbose_name='Неделя 1'),
        ),
        migrations.AlterField(
            model_name='semester',
            name='Week10',
            field=models.CharField(blank=True, max_length=255, verbose_name='Неделя 10'),
        ),
        migrations.AlterField(
            model_name='semester',
            name='Week11',
            field=models.CharField(blank=True, max_length=255, verbose_name='Неделя 11'),
        ),
        migrations.AlterField(
            model_name='semester',
            name='Week12',
            field=models.CharField(blank=True, max_length=255, verbose_name='Неделя 12'),
        ),
        migrations.AlterField(
            model_name='semester',
            name='Week13',
            field=models.CharField(blank=True, max_length=255, verbose_name='Неделя 13'),
        ),
        migrations.AlterField(
            model_name='semester',
            name='Week14',
            field=models.CharField(blank=True, max_length=255, verbose_name='Неделя 14'),
        ),
        migrations.AlterField(
            model_name='semester',
            name='Week15',
            field=models.CharField(blank=True, max_length=255, verbose_name='Неделя 15'),
        ),
        migrations.AlterField(
            model_name='semester',
            name='Week16',
            field=models.CharField(blank=True, max_length=255, verbose_name='Неделя 16'),
        ),
        migrations.AlterField(
            model_name='semester',
            name='Week2',
            field=models.CharField(blank=True, max_length=255, verbose_name='Неделя 2'),
        ),
        migrations.AlterField(
            model_name='semester',
            name='Week3',
            field=models.CharField(blank=True, max_length=255, verbose_name='Неделя 3'),
        ),
        migrations.AlterField(
            model_name='semester',
            name='Week4',
            field=models.CharField(blank=True, max_length=255, verbose_name='Неделя 4'),
        ),
        migrations.AlterField(
            model_name='semester',
            name='Week5',
            field=models.CharField(blank=True, max_length=255, verbose_name='Неделя 5'),
        ),
        migrations.AlterField(
            model_name='semester',
            name='Week6',
            field=models.CharField(blank=True, max_length=255, verbose_name='Неделя 6'),
        ),
        migrations.AlterField(
            model_name='semester',
            name='Week7',
            field=models.CharField(blank=True, max_length=255, verbose_name='Неделя 7'),
        ),
        migrations.AlterField(
            model_name='semester',
            name='Week8',
            field=models.CharField(blank=True, max_length=255, verbose_name='Неделя 8'),
        ),
        migrations.AlterField(
            model_name='semester',
            name='Week9',
            field=models.CharField(blank=True, max_length=255, verbose_name='Неделя 9'),
        ),
    ]
