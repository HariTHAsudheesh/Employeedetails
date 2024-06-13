from django import forms
from empapp.models import company

class CompanyForm(forms.ModelForm):

    class Meta:
        model=company
        fields="__all__"

        widgets={
            'cmpname':forms.TextInput(attrs={'class':'form-control'}),
            'empname':forms.TextInput(attrs={'class':'form-control'}),
            'empQuali':forms.TextInput(attrs={'class':'form-control'}),
            'empDept':forms.TextInput(attrs={'class':'form-control'}),
            'empDsg':forms.TextInput(attrs={'class':'form-control'}),
            'emgImg':forms.FileInput(attrs={'class':'form-control'}),
            'empJdate':forms.DateInput(attrs={'class':'form-control'}),
            'empSalary':forms.NumberInput(attrs={'class':'form-control'}),
            'empPhone':forms.NumberInput(attrs={'class':'form-control'}),
        }