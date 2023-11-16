from django.contrib import admin

# Register your models here.

from interview.models import Candidate
# from django.urls import reverse
# from django.utils.html import format_html

from django.http import HttpResponse
import csv
from datetime import datetime

import logging
logger = logging.getLogger('log')

exportable_fields = ['username', 'city', 'phone', 'bachelor_school', 'master_school', 'degree',
                     'first_result', 'first_interviewer_user', 'second_result', 'second_interviewer_user',
                     'hr_result', 'hr_score', 'hr_remark', 'hr_interviewer_user',]

def export_as_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    field_list = exportable_fields
    response['Content-Disposition'] = 'attachment; filename=candidates-list-%s.csv' % (
        datetime.now().strftime('%Y-%m-%d-%H-%M-%S'),
    )

    ## 写入表头
    writer = csv.writer(response)
    writer.writerow(
        [ queryset.model._meta.get_field(f).verbose_name.title()  for f in field_list ]
    )
    for obj in queryset:
        ## 单行的记录（各个字段的值），写入到csv文件
        csv_line_values = []
        for field in field_list:
            field_object = queryset.model._meta.get_field(field)
            field_value = field_object.value_from_object(obj)
            csv_line_values.append(field_value)
        writer.writerow(csv_line_values)

    logger.info("%s exported %s candidate records" % (request.user, len(queryset)))

    return response
export_as_csv.short_description = u"导出CSV文件"

#候选人管理类
class CandidateAdmin(admin.ModelAdmin):
    exclude = ('creator', 'created_date', 'modified_date')
    actions = [export_as_csv,]

    # #添加批量添加用户信息的按钮
    # def custom_button(self, request):
    #     url = reverse('upload_csv')
    #     return format_html('<a class="button" href="{}">上传 CSV 文件</a>', url)
    #
    # custom_button.short_description = '批量上传招聘者信息'

    list_display = (
        'username', 'city', 'phone', 'bachelor_school', 'first_interviewer_user', 'first_score', 'first_result',
        'second_result', 'second_interviewer_user', 'hr_interviewer_user', 'hr_score', 'hr_result', 'last_editor',
    )

    #筛选条件
    list_filter = ('username', 'first_result', 'second_result', 'hr_result', 'first_interviewer_user', 'second_interviewer_user', 'hr_interviewer_user',)

    #查询字段
    search_fields = (
        'username', 'email', 'phone', 'city', 'bachelor_school', 'first_result', 'second_result', 'second_interviewer_user',
        'hr_score', 'hr_result'
    )

    #默认字段的排序，首先是hr面试结果 > 二面结果 > 一面结果
    ordering = ['hr_result', 'second_result', 'first_result']

    default_list_editable =  ('first_interviewer_user', 'second_interviewer_user',)

    def get_list_editable(self, request):
        group_names = self.get_group_names(request.user)

        if request.user.is_superuser or 'hr' in group_names:
            return self.default_list_editable
        return ()

    def get_changelist_instance(self, request):
        self.list_editable = self.get_list_editable(request)
        return super(CandidateAdmin, self).get_changelist_instance(request)



    # 方式一：设置只读字段,所有人都不可修改
    # readonly_fields = ('first_interviewer_user', 'second_interviewer_user',)

    # 方式二：只有hr可以修改，面试官只读
    def get_group_names(self, user):
        group_names = []
        for g in user.groups.all():
            group_names.append(g.name)
        return group_names

    def get_readonly_fields(self, request, obj):
        group_names = self.get_group_names(request.user)

        if 'interviewer' in group_names:
            logger.info('interviewer is in user group for %s' % request.user.username)
            return ('first_interviewer_user', 'second_interviewer_user',)
        return ()

    #分页显示，分组展示字段，分为三块【基础信息，第一轮面试，第二轮面试（专业复试），HR终面】
    fieldsets = (
        (None, {'fields': ("userid",("username","city","phone"),("email","apply_position","born_address"),("gender","candidate_remark"),("bachelor_school","master_school","doctor_school"),("major","degree"),("test_score_of_general_ability"),"paper_score","last_editor",)}),
        ('第一轮面试记录', {'fields': (("first_score"),("first_learning_ability","first_professional_competency"),("first_advantage","first_disadvantage"),"first_result","first_recommend_position","first_interviewer_user","first_remark",)}),
        ('第二轮专业复试记录', {'fields': (("second_score"),("second_learning_ability","second_professional_competency"),("second_pursue_of_excelence","second_communication_ability","second_pressure_score"),"second_advantage","second_disadvantage","second_result","second_recommend_position","second_interviewer_user","second_remark",)}),
        ('HR第三轮终面记录', {'fields': ("hr_score",("hr_responsibility","hr_communication_ability","hr_logic_ability"),("hr_potebtial","hr_stability"),"hr_advantage","hr_disadvantage","hr_result","hr_interviewer_user","hr_remark",)}),
    )
admin.site.register(Candidate, CandidateAdmin)



