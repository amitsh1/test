from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm,TForm
from .utils import insert_csv_to_db
from .tables import RentTable,PropertyTable
from .models import Rent,Concat
from .filters import RentFilter

from django_tables2 import RequestConfig
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin

import itertools
import json
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
        PropertySqft_max = float("inf")  


    for key,group in itertools.groupby(Rent.objects.order_by('PropertyName'), lambda s: s.PropertyName):
        group = list(group)
        if PropertySqft_min<group[0].PropertySqft<PropertySqft_max:
            result.append({
                "PropertyName": key,
                "tenents": ",".join([rent.TenantName for rent in group]),
                "PropertySqft":group[0].PropertySqft
            })

    
    return render(request, 'table2.html', 
    {
        'form':form,
        'data': {




        "columns":["PropertyName","tenents", "PropertySqft"],
        "rows":result
                },     
    }
    )   

# def table(request):
#     print(request.GET.get("PropertySqft_max"))
#     if request.GET.get("PropertySqft_min") and request.GET.get("PropertySqft_min")!="":
#         PropertySqft_min = eval(request.GET.get("PropertySqft_min"))
#     else:
#         PropertySqft_min =0 
#     if request.GET.get("PropertySqft_max") and request.GET.get("PropertySqft_max")!="":
#         PropertySqft_max = eval(request.GET.get("PropertySqft_max")  )
#     else:
#         PropertySqft_max = float("inf")      
#     print(PropertySqft_max,'PropertySqft_max',PropertySqft_min,"PropertySqft_min")
#     result = []
#     for key,group in itertools.groupby(Rent.objects.order_by('PropertyName'), lambda s: s.PropertyName):
#         group = list(group)
#         if PropertySqft_min<group[0].PropertySqft<PropertySqft_max:
#             result.append({
#                 "PropertyName": key,
#                 "tenents": [rent.TenantName for rent in group],
#                 "PropertySqft":group[0].PropertySqft
#             })

    
#     table = PropertyTable(result)
#     RequestConfig(request).configure(table)
#     return render(request, "table.html", {
#         "table": table,
#         "filter":RentFilter,
#         "PropertySqft_max":3
#     })

 

class FilteredPersonListView(SingleTableMixin, FilterView):



    table_class = PropertyTable
    # table_data = result
    # model = Rent
    template_name = "table.html"

    filterset_class = RentFilter
    def get_queryset(self, **kwargs):
        print(self.request.GET,
        type(Rent.objects.all())
        )
        result = []
        for key,group in itertools.groupby(Rent.objects.order_by('PropertyName'), lambda s: s.PropertyName):
            group = list(group)
        
            result.append({
                "PropertyName": key,
                "tenents": [rent.TenantName for rent in group],
                "PropertySqft":group[0].PropertySqft
            })  
        # none_qs = Rent.objects.none()
        # qs = list(itertools.chain(none_qs, result))            
        # return Rent.objects.values('PropertyName').annotate(values=Concat('TenantName'))
        return Rent.objects.raw('SELECT * FROM okapi_rent')