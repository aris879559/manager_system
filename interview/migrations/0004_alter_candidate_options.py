# Generated by Django 4.2.1 on 2023-11-19 07:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interview', '0003_alter_candidate_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='candidate',
            options={'permissions': [('export', '可以导出数据列表'), ('notify', '通知面试官对候选人进行评估')], 'verbose_name': '应聘者信息', 'verbose_name_plural': '应聘者信息'},
        ),
    ]
