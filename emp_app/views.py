from django.shortcuts import render,HttpResponse
from .models import Department,Employee,Role
from datetime import datetime
from django.db.models import Q
# Create your views here.
def home(request):
    return render(request,'emp/home.html')

def all_emp(request):
    emps=Employee.objects.all()
    context={
        'emps':emps
    }
    # print(context)
    return render(request,'emp/all_emp.html',context)

def add_emp(request):
    if request.method=='POST':
        first_name=request.POST.get('firstname')
        last_name=request.POST.get('lastname')
        dept=int(request.POST.get('dept'))
        salary=int(request.POST.get('salary'))
        bonus=int(request.POST.get('bonus'))
        role=int(request.POST.get('role'))
        phone=int(request.POST.get('phone'))
        hire_date=request.POST.get('hiredate')
        emp=Employee(first_name=first_name,last_name=last_name,dept_id=dept,salary=salary,bonus=bonus,role_id=role,phone=phone,hire_date=datetime.today())
        emp.save()
        return HttpResponse("<h1>Employee Added SuccessFully</h1>")
    elif request.method=='GET':
        return render(request,'emp/add_emp.html')
    else:
        return HttpResponse("An Exception Occured! Employee Has Not been Added")

def remove_emp(request,emp_id=0):
    if emp_id:
        try:
            emp_to_be_removed=Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("<h1>employee Removed SuccessFully<h1>")
        except:
            return HttpResponse(("Please Enter A Valid EMPID"))
    emps=Employee.objects.all()
    context={
        'emps':emps
    }
    return render(request,'emp/remove_emp.html',context)

def filter_emp(request):
    if request.method=='POST':
        name=request.POST['name']
        dept=request.POST['dept']
        role=request.POST['role']
        emps=Employee.objects.all()
        if name:
            emps=emps.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))
        if dept:
            emps=emps.filter(dept__name__icontains=dept)
        if role:
            emps=emps.filter(role__name__icontains=role)
        return render(request,'emp/all_emp.html',{'emps':emps})
    
    elif request.method=='GET':
        return render(request,'emp/filter_emp.html')
    else:
        return HttpResponse('An Exception Occured')
