from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm,TForm
from .utils import insert_csv_to_db
from .models import Rent,Concat

from django.contrib import messages



import itertools
import json


def upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            insert_csv_to_db(request.FILES['file'])
            messages.info(request, 'Your file was uploaded successfully!')
            return HttpResponseRedirect('/')            

    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})    



def tt(request):
    result = []
    form = TForm(request.GET)
    if form.data.get("PropertySqft_min") and form.data.get("PropertySqft_min")!="":
        PropertySqft_min = eval(form.data.get("PropertySqft_min"))
    else:
        PropertySqft_min =0 
    if form.data.get("PropertySqft_max") and form.data.get("PropertySqft_max")!="":
        PropertySqft_max = eval(form.data.get("PropertySqft_max")  )
    else:
        PropertySqft_max = 999999999 


    for key,group in itertools.groupby(
        Rent.objects.filter(
            UnitSqft__gte=PropertySqft_min,
            UnitSqft__lte = PropertySqft_max
            ).order_by('PropertyName'), lambda s: s.PropertyName):
        group = list(group)
        result.append({
            "PropertyName": key,
            "City":group[0].City,
            "tenents": ",".join([rent.TenantName for rent in sorted(group,key=lambda x: x.UnitSqft)]),
            
        })

    
    return render(request, 'table2.html', 
    {
        'form':form,
        'data': {




        "columns":["PropertyName","City","tenents"],
        "rows":result
                },     
    }
    )   
