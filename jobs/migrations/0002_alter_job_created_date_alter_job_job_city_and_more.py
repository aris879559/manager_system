# Generated by Django 4.2.1 on 2023-11-06 09:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='创建日期'),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_city',
            field=models.SmallIntegerField(choices=[[0, '北京'], [1, '上海'], [2, '深圳']], verbose_name='工作地点'),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_requirement',
            field=models.TextField(max_length=1024, verbose_name='职位要求'),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_type',
            field=models.SmallIntegerField(choices=[(0, '技术类'), (1, '产品类'), (2, '运营类'), (3, '设计类')], verbose_name='职位类别'),
        ),
        migrations.AlterField(
            model_name='job',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='修改日期'),
        ),
    ]
