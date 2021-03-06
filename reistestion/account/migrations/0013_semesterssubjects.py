# Generated by Django 3.2.2 on 2021-11-19 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_auto_20211116_1839'),
    ]

    operations = [
        migrations.CreateModel(
            name='SemestersSubjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Semester', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='account.semester', verbose_name='Semester_key')),
                ('Subject', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='account.subjectsnames', verbose_name='Subject_key')),
            ],
        ),
    ]
