# Generated by Django 2.2.4 on 2019-09-02 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('telphone', models.IntegerField()),
                ('province', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('town', models.CharField(max_length=200)),
                ('addr', models.CharField(max_length=200)),
                ('date', models.DateField(auto_now_add=True)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('kd', models.CharField(max_length=200)),
                ('obj_type', models.CharField(max_length=200)),
                ('send_name', models.CharField(max_length=200)),
                ('send_tel', models.IntegerField()),
                ('send_bumen', models.CharField(max_length=200)),
                ('send_addr', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='发布时间')),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Question')),
            ],
        ),
    ]
