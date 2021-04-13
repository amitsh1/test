from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
from .utils import insert_csv_to_db
from .tables import RentTable
from .models import Rent

from django_tables2 import RequestConfig
# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

def upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            insert_csv_to_db(request.FILES['file'])
            return HttpResponse("Hello, world. You're at the polls index.")
            # return HttpResponseRedirect('/upload')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})    


def table(request):
    table = RentTable(Rent.objects.all())
    RequestConfig(request).configure(table)
    return render(request, "table.html", {
        "table": table
    })

 