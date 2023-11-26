from django.contrib import admin

from jobs.models import Job,Resume
# Register your models here.

#创建人默认是当前用户
class JobAdmin(admin.ModelAdmin):
    exclude = ['creater', 'created_date', 'modified_date']
    list_display = ['job_name', 'job_type', 'job_city', 'creater', 'created_date', 'modified_date']
    list_filter = ['job_name', 'job_type', 'job_city', 'creater', 'created_date', 'modified_date']
    search_fields = ['job_name', 'job_type', 'job_city', 'creater', 'created_date', 'modified_date']
    list_per_page = 10
    def save_model(self, request, obj, form, change):
        obj.creater = request.user
        super().save_model(request, obj, form, change)


class ResumeAdmin(admin.ModelAdmin):
    # exclude = ['applicant', 'created_date', 'modified_date']
    list_display = ('username', 'applicant', 'city', 'apply_position', 'bachelor_school', 'master_school', 'major', 'created_date')
    list_filter = ('username', 'applicant', 'city', 'apply_position', 'bachelor_school', 'master_school', 'major')
    readonly_fields = ('applicant', 'created_date',  'modified_date')

    fieldsets = (
        (None,{'fields':(
            "applicant",("username","city","phone"),
            ("email","apply_position","born_address","gender",),
            ("bachelor_school","master_school"),("major","degree"),("created_date","modified_date"),
            "candidate_introduction", )}),
    )

    def save_model(self, request, obj, form, change):
        obj.applicant = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Job, JobAdmin)
admin.site.register(Resume, ResumeAdmin)