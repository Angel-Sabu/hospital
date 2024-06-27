from django.shortcuts import render, redirect
from HospitalBackend.models import DepDB, DoctorDB, LaborataryDB
from HospitalFrontend.models import signupDB, appoinmentDB, contactDB, feedbackDB, LabappoDB


# Create your views here.

def homepage(request):
    return render(request, "home.html")


def departmentpage(request):
    dep = DepDB.objects.all()
    return render(request, "department.html", {'dep': dep})


def departmentsinglepages(request, proid):
    data = DepDB.objects.get(id=proid)
    return render(request, "departmentsingle.html", {'data': data})


def doctorspages(request):
    doc = DoctorDB.objects.all()
    return render(request, "doctors.html", {'doc': doc})


def filter_doctor(request, dep_name):
    data = DoctorDB.objects.filter(Departmentname=dep_name)
    return render(request, "filterdoctor.html", {'data': data})


def doctorsinglepage(request, docid):
    data = DoctorDB.objects.get(id=docid)
    return render(request, "doctors_single.html", {'data': data})


def signuppage(request):
    return render(request, "signup.html")


def signupsave(request):
    if request.method == "POST":
        n = request.POST.get('Name')
        e = request.POST.get('Email')
        u = request.POST.get('Username')
        r = request.POST.get('RegPassword')
        obj = signupDB(Name=n, Email=e, Username=u, RegPassword=r)
        obj.save()
        return redirect(signuppage)


def loginpage(request):
    return render(request, "signup.html")


def userlogin(request):
    if request.method == "POST":
        un = request.POST.get('Username')
        pwd = request.POST.get('loginpassword')
        if signupDB.objects.filter(Username=un, RegPassword=pwd).exists():
            request.session['Username'] = un
            request.session['RegPassword'] = pwd
            return redirect(homepage)
        else:
            return redirect(signuppage)

    return redirect(signuppage)


def logout(request):
    del request.session['Username']
    del request.session['RegPassword']
    return redirect(loginpage)


def appoinment(request, docid):
    data = DoctorDB.objects.get(id=docid)
    return render(request, "Appoinment.html", {'data': data})


def saveappoinment(request):
    if request.method == "POST":
        pn = request.POST.get('patientname')
        pd = request.POST.get('patientdob')
        apd = request.POST.get('AppoinmentDate')
        pt = request.POST.get('patienttime')
        pnu = request.POST.get('patientnumber')
        pde = request.POST.get('patientdes')
        do = request.POST.get('doc_name')
        de = request.POST.get('Departmentname')
        st = request.POST.get('Status')
        un = request.POST.get('UserName')
        obj = appoinmentDB(patientname=pn, patientdob=pd, AppoinmentDate=apd, patienttime=pt, patientnumber=pnu,
                           patientdes=pde,Status=st,
                           Departmentname=de, doc_name=do, UserName=un)
        obj.save()
        return redirect(confirmationpage)


def aboutpage(request):
    return render(request, 'about.html')


def contactpage(request):
    return render(request, 'contact.html')


def savecontact(request):
    if request.method == "POST":
        n = request.POST.get('name')
        e = request.POST.get('email')
        p = request.POST.get('phone')
        m = request.POST.get('message')
        a = request.POST.get('address')
        obj = contactDB(name=n, email=e, phone=p, message=m, address=a)
        obj.save()
        return redirect(contactpage)


def servicepage(request):
    return render(request, 'service.html')


def confirmationpage(request):
    return render(request, 'confirmation.html')


def appoinmentviewpage(request):
    data = appoinmentDB.objects.filter(UserName=request.session['Username'])
    return render(request, "Appoinmentview.html", {'data': data})


def deleteappoinment(request, dataid):
    cart = appoinmentDB.objects.filter(id=dataid)
    cart.delete()
    return redirect(appoinmentviewpage)


def feedback(request):
    return render(request, "feedback.html")


def savefeedback(request):
    if request.method == "POST":
        n = request.POST.get('Name')
        f = request.POST.get('Feedback')
        obj = feedbackDB(Name=n, Feedback=f)
        obj.save()
        return redirect(feedback)


def feedbackviewpage(request):
    data = feedbackDB.objects.all()
    return render(request, "feedbackview.html", {'data': data})


def deletefeedback(request, dataid):
    cart = feedbackDB.objects.filter(id=dataid)
    cart.delete()
    return redirect(feedbackviewpage)


def labpage(request):
    lab = LaborataryDB.objects.all()
    return render(request, "Labpage.html", {'lab': lab})


def LabAppoinment(request, labid):
    data = LaborataryDB.objects.get(id=labid)
    return render(request, "LabAppoinment.html", {'data': data})


def savelabappoinment(request):
    if request.method == "POST":
        pn = request.POST.get('patientsname')
        pd = request.POST.get('patientsdob')
        pt = request.POST.get('patientstime')
        pnu = request.POST.get('patientsnumber')
        pde = request.POST.get('patientsdes')
        de = request.POST.get('Testname')
        S = request.POST.get('Status')
        un = request.POST.get('UserName')
        obj = LabappoDB(patientsname=pn, patientsdob=pd, patientstime=pt, patientsnumber=pnu, patientsdes=pde,
                        Testname=de,Status=S, UserName=un)
        obj.save()
        return redirect(labconfirmationpage)


def labconfirmationpage(request):
    return render(request, "labconfirmation.html")


def labappoinmentview(request):
    data = LabappoDB.objects.filter(UserName=request.session['Username'])
    return render(request, "LabAppoinmentview.html", {'data': data})


def deletelabappoinment(request, dataid):
    labcart = LabappoDB.objects.filter(id=dataid)
    labcart.delete()
    return redirect(labappoinmentview)
