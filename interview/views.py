from django.shortcuts import render

# Create your views here.

import csv
from interview.models import Candidate

def import_candidate_from_csv(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)  # 跳过CSV文件的标题行
        for row in reader:
            candidate = Candidate(
                username=row[0],
                city=row[1],
                phone=row[2],
                bachelor_school=row[3],
                major=row[4],
                degree=row[5],
                test_score_of_general_ability=row[6],
                paper_score=row[7]
            )
            candidate.save()

from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from interview.views import import_candidate_from_csv
from django.http import HttpResponse

def upload_csv(request):
    if request.method == 'POST' and request.FILES['csv_file']:
        csv_file = request.FILES['csv_file']
        fs = FileSystemStorage()
        file_path = fs.save(csv_file.name, csv_file)
        import_candidate_from_csv(file_path)
        return HttpResponse("CSV文件上传成功")
    return render(request, 'upload_csv.html')
