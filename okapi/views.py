from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm

# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

def index(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})    