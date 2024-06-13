from django.shortcuts import render,redirect

from empapp.models import company

from django.views.generic import View

from empapp.forms import CompanyForm

#create your views here

#view for listing all employees

# def employe_list_view(request,*args,**kwargs):
#     qs=company.objects.all()
#     return render(request,"employee_list.html",{'data':qs})

class EmployeListView(View):
    def get(self,request,*args,**kwargs):

        qs=company.objects.all()

        return render(request,"employee_list.html",{'data':qs})


#url:localhost:8000/empapp/employe/add/
#method:get,post

class EmployecreateView(View):
    def get(self,request,*args,**kwargs):
        print("inside get")

        form=CompanyForm()
        return render(request,"employe_add.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        print("POST DATA",request.POST)

        form=CompanyForm(request.POST,files=request.FILES)
        if form.is_valid():
            data=form.cleaned_data
            company.objects.create(**data)
            return redirect("employee-list")
        
        return render(request,"employe_add.html", {"form":form})



# employe detail view
# localhost:800/empapp/company/{id}/
    # method:get

class EmployeDetailView(View):
    def get(self,request,*args,**kwargs):
        print(kwargs)
        id=kwargs.get("pk")
        qs=company.objects.get(id=id)
        return render(request,"employe_detail.html",{'data':qs})
    
# employee deleteview
    # url:localhost:8000/empapp/company/{id}/remove
    # method:get

class EmployeeDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        company.objects.get(id=id).delete()
        return redirect("employee-list")
    
# url:localhost:8000/empapp/company/{id}/change/
# method=get,post

class EmployeUpdateView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        company_objects=company.objects.get(id=id)
        form=CompanyForm(instance=company_objects)
        return render(request,"employe_edit.html",{'form':form})
    
    def post(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        company_objects=company.objects.get(id=id)
        form=CompanyForm(request.POST,files=request.FILES,instance=company_objects)
        if form.is_valid():
            form.save()
            return redirect('employee-list')
        else:
            return render(request,"employe_edit.html",{"form":form})

