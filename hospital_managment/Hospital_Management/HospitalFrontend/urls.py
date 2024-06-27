from django.urls import path
from HospitalFrontend import views

urlpatterns = [

    path('homepage/', views.homepage, name="homepage"),
    path('departmentpage/', views.departmentpage, name="departmentpage"),
    path('departmentsinglepages/<int:proid>/', views.departmentsinglepages, name="departmentsinglepages"),

    path('doctorspages/', views.doctorspages,name="doctorspages"),
    path('filter_doctor/<dep_name>/', views.filter_doctor, name="filter_doctor"),

    path('doctorsinglepage/<int:docid>/', views.doctorsinglepage,name="doctorsinglepage"),

    path('signuppage/', views.signuppage, name="signuppage"),
    path('signupsave/', views.signupsave, name="signupsave"),
    path('loginpage/', views.loginpage, name="loginpage"),
    path('userlogin/', views.userlogin, name="userlogin"),
    path('logout/', views.logout, name="logout"),

    path('appoinment/<int:docid>/', views.appoinment, name="appoinment"),
    path('saveappoinment/', views.saveappoinment, name="saveappoinment"),


    path('aboutpage/', views.aboutpage, name="aboutpage"),
    path('servicepage/', views.servicepage, name="servicepage"),
    path('confirmationpage/', views.confirmationpage, name="confirmationpage"),

    path('contactpage/', views.contactpage, name="contactpage"),
    path('savecontact/', views.savecontact, name="savecontact"),

    path('feedback/', views.feedback, name="feedback"),
    path('savefeedback/', views.savefeedback, name="savefeedback"),
    path('feedbackviewpage/', views.feedbackviewpage, name="feedbackviewpage"),
    path('deletefeedback/<int:dataid>/', views.deletefeedback, name="deletefeedback"),

    path('appoinmentviewpage/', views.appoinmentviewpage, name="appoinmentviewpage"),
    path('deleteappoinment/<int:dataid>/', views.deleteappoinment, name="deleteappoinment"),

    path('labpage/', views.labpage, name="labpage"),
    path('savelabappoinment/', views.savelabappoinment, name="savelabappoinment"),
    path('LabAppoinment/<int:labid>/', views.LabAppoinment, name="LabAppoinment"),
    path('labconfirmationpage/', views.labconfirmationpage, name="labconfirmationpage"),
    path('labappoinmentview/', views.labappoinmentview, name="labappoinmentview"),
    path('deletelabappoinment/<int:dataid>/', views.deletelabappoinment, name="deletelabappoinment"),




]