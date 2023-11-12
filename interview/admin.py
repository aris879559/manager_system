from django.contrib import admin

# Register your models here.

from interview.models import Candidate
from django.urls import reverse
from django.utils.html import format_html


class CandidateAdmin(admin.ModelAdmin):
    exclude = ('creator', 'created_date', 'modified_date')

    #添加批量添加用户信息的按钮
    def custom_button(self, request):
        url = reverse('upload_csv')
        return format_html('<a class="button" href="{}">上传 CSV 文件</a>', url)

    custom_button.short_description = '批量上传招聘者信息'

    list_display = (
        'username', 'city', 'phone', 'bachelor_school', 'first_score', 'first_result',
        'second_result', 'second_interviewer', 'hr_score', 'hr_result', 'last_editor', 'custom_button'
    )
    #分页显示，分组展示字段，分为三块【基础信息，第一轮面试，第二轮面试（专业复试），HR终面】
    fieldsets = (
        (None, {'fields': ("userid",("username","city","phone"),("email","apply_position","born_address"),("gender","candidate_remark"),("bachelor_school","master_school","doctor_school"),("major","degree"),("test_score_of_general_ability"),"paper_score","last_editor",)}),
        ('第一轮面试记录', {'fields': (("first_score","first_learning_ability","first_professional_competency"),("first_advantage","first_disadvantage"),"first_result","first_recommend_position","first_interviewer","first_remark",)}),
        ('第二轮专业复试记录', {'fields': (("second_score","second_learning_ability","second_professional_competency"),("second_pursue_of_excelence","second_communication_ability","second_pressure_score"),"second_advantage","second_disadvantage","second_result","second_recommend_position","second_interviewer","second_remark",)}),
        ('HR第三轮终面记录', {'fields': ("hr_score",("hr_responsibility","hr_communication_ability","hr_logic_ability"),("hr_potebtial","hr_stability"),"hr_advantage","hr_disadvantage","hr_result","hr_interviewer","hr_remark",)}),
    )

    #筛选条件
    list_filter = ('username', 'first_result', 'second_result', 'hr_result', 'first_interviewer', 'second_interviewer', 'hr_interviewer',)

    #查询字段
    search_fields = (
        'username', 'email', 'phone', 'city', 'bachelor_school', 'first_result', 'second_result', 'second_interviewer',
        'hr_score', 'hr_result'
    )

    #默认字段的排序，首先是hr面试结果 > 二面结果 > 一面结果
    ordering = ['hr_result', 'second_result', 'first_result']

admin.site.register(Candidate, CandidateAdmin)



