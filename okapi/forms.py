from django import forms

class UploadFileForm(forms.Form):
    # title = forms.CharField(max_length=50)
    file = forms.FileField()


class TForm(forms.Form):
    PropertySqft_min = forms.IntegerField(required=False)    
    PropertySqft_max = forms.IntegerField(required=False)  


