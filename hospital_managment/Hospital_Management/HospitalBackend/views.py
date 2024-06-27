from django.shortcuts import render, redirect, get_object_or_404, reverse
from HospitalBackend.models import DepDB, DoctorDB, LaborataryDB
from HospitalFrontend.models import LabappoDB, appoinmentDB
from HospitalFrontend.views import appoinmentviewpage
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.template.loader import get_template
from django.http import HttpResponse


# Create your views here.

def dashboard(request):
    appoinment = appoinmentDB.objects.all()
    labappoinment = LabappoDB.objects.all()
    doctor = DoctorDB.objects.all()
    Deparnment = DepDB.objects.all()
    Laboratary = LaborataryDB.objects.all()
    a = 0
    l = 0
    d = 0
    p = 0
    la = 0
    for i in appoinment:
        a += 1
    for i in labappoinment:
        l += 1
    for i in doctor:
        d += 1
    for i in Deparnment:
        p += 1
    for i in Laboratary:
        la += 1
    d1 = {'a': a, 'l': l, 'd': d, 'p': p, 'la': la}

    return render(request, "dashboard.html", d1)


def indexpage(request):
    return render(request, "index.html")


def departmentpages(request):
    return render(request, "add_department.html")


def DepartmentSave(request):
    if request.method == "POST":
        n = request.POST.get('Departmentname')
        d = request.POST.get('Description')
        s = request.POST.get('Services')
        i = request.FILES['DepartmentImages']
        obj = DepDB(Departmentname=n, Description=d, Services=s, DepartmentImages=i)
        obj.save()
        messages.success(request, "Department Saved SuccessFully...!!")
        return redirect(departmentpages)


def viewdepartment(request):
    data = DepDB.objects.all()
    return render(request, 'displaydepartment.html', {'data': data})


def departmentedit(request, dataid):
    dep = DepDB.objects.get(id=dataid)
    return render(request, "departmentedit.html", {'dep': dep})


def updatedepartment(request, dataid):
    if request.method == "POST":
        cn = request.POST.get('Departmentname')
        des = request.POST.get('Description')
        se = request.POST.get('Services')
        try:
            img = request.FILES['DepartmentImages']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = DepDB.objects.get(id=dataid).DepartmentImages
        DepDB.objects.filter(id=dataid).update(Departmentname=cn, Description=des, Services=se, DepartmentImages=file)
        messages.success(request, "Category Edited SuccessFully...!!")
        return redirect(viewdepartment)


def deletedepartment(request, dataid):
    dep = DepDB.objects.filter(id=dataid)
    dep.delete()
    return redirect(viewdepartment)


def doctorpage(request):
    department = DepDB.objects.all()
    return render(request, "adddoctor.html", context={"department": department})


def doctorsave(request):
    if request.method == "POST":
        dna = request.POST.get('doc_name')
        ds = request.POST.get('doc_spec')
        dos = request.POST.get('doc_desc')
        dn = request.POST.get('Departmentname')
        di = request.FILES['doc_image']
        obj = DoctorDB(doc_name=dna, doc_spec=ds, doc_desc=dos, Departmentname=dn, doc_image=di)
        obj.save()
        messages.success(request, "Product Saved SuccessFully...!!")
        return redirect(doctorpage)


def doctordisplay(request):
    data = DoctorDB.objects.all()
    return render(request, "doctordisplay.html", {'data': data})


def doctoredit(request, dataid):
    doc = DoctorDB.objects.get(id=dataid)
    department = DepDB.objects.all()
    return render(request, "doctoredit.html", {'doc': doc, 'department': department})


def updatedoctor(request, dataid):
    if request.method == "POST":
        dna = request.POST.get('doc_name')
        ds = request.POST.get('doc_spec')
        doss = request.POST.get('doc_desc')
        dn = request.POST.get('Departmentname')
        try:
            img = request.FILES['doc_image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = DoctorDB.objects.get(id=dataid).doc_image
        DoctorDB.objects.filter(id=dataid).update(doc_name=dna, doc_spec=ds, doc_desc=doss, Departmentname=dn,
                                                  doc_image=file)
        messages.success(request, "Product Edited SuccessFully...!!")
        return redirect(doctordisplay)


def deletedoctor(request, dataid):
    doc = DoctorDB.objects.filter(id=dataid)
    doc.delete()
    return redirect(doctordisplay)


def loginpage(request):
    return render(request, "login.html")


def adminlogin(request):
    if request.method == "POST":
        un = request.POST.get('user_name')
        pw = request.POST.get('pass_word')
        if User.objects.filter(username__contains=un).exists():
            user = authenticate(username=un, password=pw)
            if user is not None:
                login(request, user)
                request.session['username'] = un
                request.session['password'] = pw
                return redirect(dashboard)

            else:
                return redirect(loginpage)
        else:
            return redirect(loginpage)


def adminlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(loginpage)


def laboratoryaddpages(request):
    return render(request, "add_labortary.html")


def laboratorysave(request):
    if request.method == "POST":
        t = request.POST.get('Testname')
        d = request.POST.get('Description')
        te = request.FILES['Testimages']
        obj = LaborataryDB(Testname=t, Description=d, Testimages=te)
        obj.save()
        messages.success(request, "Laboratory Saved SuccessFully...!!")
        return redirect(laboratoryaddpages)


def viewlab(request):
    data = LaborataryDB.objects.all()
    return render(request, "LabDisplay.html", {'data': data})


def Labedit(request, dataid):
    lab = LaborataryDB.objects.get(id=dataid)
    return render(request, "editlab.html", {'lab': lab})


def updatelab(request, dataid):
    if request.method == "POST":
        cn = request.POST.get('Testname')
        des = request.POST.get('Description')
        try:
            img = request.FILES['Testimages']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = LaborataryDB.objects.get(id=dataid).Testimages
        LaborataryDB.objects.filter(id=dataid).update(Testname=cn, Description=des, Testimages=file)
        messages.success(request, "Laboratory Edited SuccessFully...!!")
        return redirect(viewlab)


def deletelab(request, dataid):
    dep = LaborataryDB.objects.filter(id=dataid)
    dep.delete()
    return redirect(viewlab)


def appoinmentlist(request):
    appoinments = appoinmentDB.objects.all()
    context = {
        'appoinments': appoinments
    }
    return render(request, 'approvedisplay.html', context)


def lablist(request):
    labs = LabappoDB.objects.all()
    context = {
        'labs': labs
    }
    return render(request, 'lab_Approve.html', context)


def approveedit(request, dataid):
    appo = appoinmentDB.objects.get(id=dataid)
    return render(request, "approveedit.html", {'appo': appo})


def updateapprove(request, dataid):
    if request.method == "POST":
        pn = request.POST.get('patientname')
        apd = request.POST.get('AppoinmentDate')
        pt = request.POST.get('patienttime')
        pnu = request.POST.get('patientnumber')
        do = request.POST.get('doc_name')
        de = request.POST.get('Departmentname')
        st = request.POST.get('Status')
        un = request.POST.get('UserName')
        appoinmentDB.objects.filter(id=dataid).update(patientname=pn, AppoinmentDate=apd, patienttime=pt, patientnumber=pnu,
                           Status=st,
                           Departmentname=de, doc_name=do, UserName=un)
        messages.success(request, "Status Edited SuccessFully...!!")
        return redirect(appoinmentlist)


def labapproveedit(request, dataid):
    appo = LabappoDB.objects.get(id=dataid)
    return render(request, "labapproveedit.html", {'appo': appo})


def labupdateapprove(request, dataid):
    if request.method == "POST":
        T = request.POST.get('Testname')
        pn = request.POST.get('patientsname')
        apd = request.POST.get('patientsdob')
        pt = request.POST.get('patientstime')
        pnu = request.POST.get('patientsnumber')
        st = request.POST.get('Status')
        un = request.POST.get('UserName')
        LabappoDB.objects.filter(id=dataid).update( Testname=T,patientsname=pn, patientsdob=apd, patientstime=pt, patientsnumber=pnu,
                           Status=st,UserName=un)
        messages.success(request, "Status Edited SuccessFully...!!")
        return redirect(lablist)
