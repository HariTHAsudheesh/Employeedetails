from django.urls import path
from empapp import views

urlpatterns=[
    # path("employe/all/",views.employe_list_view,name="employee-list"),
    path("employe/all/",views.EmployeListView.as_view(),name="employee-list"),

    path("employe/add/",views.EmployecreateView.as_view(),name="employe-add"),
    
    path("employe/<int:pk>/",views.EmployeDetailView.as_view(),name='employe-detail'),

    path("employe/<int:pk>/remove/",views.EmployeeDeleteView.as_view(),name="employe-remove"),

    path("employe/<int:pk>/change/",views.EmployeUpdateView.as_view(),name="employe-edit"),

   
]
