from django.shortcuts import render

# Create your views here.
from django.template import loader
from django.http import HttpResponse
from jobs.models import Job
from jobs.models import JobType, Cities

def joblist(request):
    job_list = Job.objects.order_by('job_type')
    template = loader.get_template('joblist.html')
    context = {
        'job_list': job_list,
    }

    for job in job_list:
        job.city_name = Cities[job.job_city]
        job.job_type = JobType[job.job_type]

    return HttpResponse(template.render(context))

def jobdetail(request, job_id):
    job = Job.objects.get(id=job_id)
    template = loader.get_template('jobs/jobdetail.html')
    context = {
        'job': job,
    }
    return HttpResponse(template.render(context, request))



