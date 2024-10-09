from django.shortcuts import render
from django.db.models import *

# Create your views here.
from app.models import *
def Emp(request):
    EDO = emp.objects.select_related().all()    
    d={'EDO':EDO}
    return render(request,'Emp.html',context=d)

def EDO(request):
    # EmpDepO = emp.objects.select_related('deptno').all()
    # d={'EmpDepO':EmpDepO}
    #print(emp.objects.all().aggregate(Avg('sal')))
    #print(emp.objects.all().aggregate(Sum('sal')))
    #print(emp.objects.values('deptno').annotate(Avg('sal')))
    #print(emp.objects.filter(deptno=20).aggregate(Avg('sal')))
    print(emp.objects.all().aggregate(Max('sal')))
    print(emp.objects.all().aggregate(Min('sal')))
    print(emp.objects.all().aggregate(Sum('sal')))
    print(emp.objects.all().aggregate(Avg('sal')))
    DOAVA = emp.objects.all().aggregate(Avg('sal'))

    #EmpDepO= emp.objects.select_related('deptno').filter(sal__gt=DOAVA['sal__avg'])
    EmpDepO= emp.objects.select_related('deptno').filter(sal__lt=DOAVA['sal__avg'])
    d={'EmpDepO':EmpDepO}
    return render(request,'EDO.html',d)

def Emps(request):
    empso = emp.objects.select_related().filter(ename__startswith='S')
    empso= emp.objects.select_related().filter(sal__gt=15000)
    empso = emp.objects.select_related().filter(comm__lt= 150)
    d ={'empso':empso}
    return render(request,'Emps.html',d)
def DeptEmp(request):
    LDEO = dept.objects.prefetch_related('emp_set').all()
    d= {'LDEO':LDEO}
    return render(request,'DeptEmp.html',d)
