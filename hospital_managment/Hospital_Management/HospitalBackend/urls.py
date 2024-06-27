from django.urls import path
from HospitalBackend import views

urlpatterns = [
    path('indexpage/', views.indexpage, name="indexpage"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('departmentpages/', views.departmentpages, name="departmentpages"),
    path('DepartmentSave/', views.DepartmentSave, name="DepartmentSave"),

    path('viewdepartment/', views.viewdepartment, name="viewdepartment"),
    path('departmentedit/<int:dataid>', views.departmentedit, name="departmentedit"),
    path('updatedepartment/<int:dataid>', views.updatedepartment, name="updatedepartment"),
    path('deletedepartment/<int:dataid>', views.deletedepartment, name="deletedepartment"),

    path('doctorpage/', views.doctorpage, name="doctorpage"),
    path('doctorsave/', views.doctorsave, name="doctorsave"),
    path('doctordisplay/', views.doctordisplay, name="doctordisplay"),
    path('appoinmentlist/', views.appoinmentlist, name="appoinmentlist"),
    path('lablist/', views.lablist, name="lablist"),
    path('approveedit/<int:dataid>', views.approveedit, name="approveedit"),
    path('updateapprove/<int:dataid>', views.updateapprove, name="updateapprove"),
    path('labapproveedit/<int:dataid>', views.labapproveedit, name="labapproveedit"),
    path('labupdateapprove/<int:dataid>', views.labupdateapprove, name="labupdateapprove"),


    path('doctoredit/<int:dataid>', views.doctoredit, name="doctoredit"),
    path('updatedoctor/<int:dataid>', views.updatedoctor, name="updatedoctor"),
    path('deletedoctor/<int:dataid>', views.deletedoctor, name="deletedoctor"),

    path('loginpage/', views.loginpage, name="loginpage"),
    path('adminlogin/',views.adminlogin, name="adminlogin"),
    path('adminlogout/',views.adminlogout, name="adminlogout"),


    path('laboratoryaddpages/',views.laboratoryaddpages, name="laboratoryaddpages"),
    path('laboratorysave/',views.laboratorysave, name="laboratorysave"),
    path('viewlab/',views.viewlab, name="viewlab"),
    path('Labedit/<int:dataid>', views.Labedit, name="Labedit"),
    path('updatelab/<int:dataid>', views.updatelab, name="updatelab"),
    path('deletelab/<int:dataid>', views.deletelab, name="deletelab"),
]