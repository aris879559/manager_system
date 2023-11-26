from django.db import models

from django.contrib.auth.models import User
from datetime import datetime
from interview.models import DEGREE_TYPE

JobType = [
    (0,"技术类"),
    (1,"产品类"),
    (2,"运营类"),
    (3,"设计类"),
]

Cities = [
    [0,'北京',],
    [1,'上海',],
    [2,'深圳',],
]
# Create your models here.
class Job(models.Model):
    job_type = models.SmallIntegerField(blank=False,choices=JobType,verbose_name='职位类别')
    job_name = models.CharField(max_length=250,blank=False,verbose_name='职位名称')
    job_city = models.SmallIntegerField(choices=Cities,blank=False,verbose_name='工作地点')
    job_reponsibility = models.TextField(max_length=1024,verbose_name='职位职责')
    job_requirement = models.TextField(max_length=1024,blank=False,verbose_name='职位要求')
    creater = models.ForeignKey(User,verbose_name='创建者',on_delete=models.SET_NULL,null=True)
    created_date = models.DateTimeField(verbose_name='创建日期',default=datetime.now)
    modified_date = models.DateTimeField(verbose_name='修改日期',default=datetime.now)

    class Meta:
        verbose_name = u'岗位信息'
        verbose_name_plural = u'岗位信息'

class Resume(models.Model):
    username = models.CharField(max_length=250,verbose_name='姓名')
    applicant = models.ForeignKey(User, verbose_name="申请人", on_delete=models.SET_NULL, null=True)
    city = models.CharField(max_length=135, verbose_name=u'城市')
    phone = models.CharField(max_length=135, verbose_name=u'手机号码')
    email = models.EmailField(max_length=135, verbose_name=u'邮箱', blank=True)
    apply_position = models.CharField(max_length=135, verbose_name=u'应聘职位', blank=True)
    born_address = models.CharField(max_length=135, verbose_name=u'生源地', blank=True)
    gender = models.CharField(max_length=135, verbose_name=u'性别', blank=True)

    # 学校与学历信息
    bachelor_school = models.CharField(max_length=135, verbose_name=u'本科学校', blank=True)
    master_school = models.CharField(max_length=135, verbose_name=u'研究生学校', blank=True)
    doctor_school = models.CharField(max_length=135, verbose_name=u'博士生学校', blank=True)
    major = models.CharField(max_length=135, verbose_name=u'专业', blank=True)
    degree = models.CharField(max_length=135, verbose_name=u'学历', blank=True, choices=DEGREE_TYPE)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    modified_date = models.DateTimeField(auto_now=True, verbose_name=u'修改时间')

    #候选人自我介绍，工作经历，项目经历
    candidate_introduction = models.TextField(verbose_name=u'自我介绍', blank=True, max_length=2048)
    work_experience = models.TextField(verbose_name=u'工作经历', blank=True, max_length=2048)
    project_experience = models.TextField(verbose_name=u'项目经历', blank=True, max_length=2048)

    class Meta:
        verbose_name = u'简历'
        verbose_name_plural = u'简历列表'