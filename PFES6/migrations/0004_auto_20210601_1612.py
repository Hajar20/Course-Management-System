# Generated by Django 3.2.3 on 2021-06-01 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PFES6', '0003_alter_course_coursefile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='correction_td_tp',
            name='corrFile',
            field=models.FileField(null=True, upload_to='documents'),
        ),
        migrations.AlterField(
            model_name='td',
            name='tdFile',
            field=models.FileField(null=True, upload_to='documents'),
        ),
        migrations.AlterField(
            model_name='tp',
            name='tpFile',
            field=models.FileField(null=True, upload_to='documents'),
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('creationDateTodo', models.DateField()),
                ('TodoTFile', models.FileField(null=True, upload_to='documents')),
                ('TodoSFile', models.FileField(null=True, upload_to='documents')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PFES6.classsubject')),
            ],
        ),
        migrations.CreateModel(
            name='JoinClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PFES6.classsubject')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PFES6.users')),
            ],
        ),
    ]