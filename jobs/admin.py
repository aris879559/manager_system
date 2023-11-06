from django.contrib import admin

from jobs.models import Job
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


admin.site.register(Job,JobAdmin)