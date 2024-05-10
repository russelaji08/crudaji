from django.shortcuts import render,redirect
from .forms import employeeform
from .models import employee
def home(reqeust):
    obj=employee.objects.all()
    return render(reqeust,'home.html',{'data':obj})
def create(reqeust):
    if reqeust.method=="POST":
        myform=employeeform(reqeust.POST)
        if myform.is_valid():
            myform.save()
            return redirect('read')
        return redirect('create')
    else:
        myform=employeeform
        return render(reqeust,'create.html',{'form':myform})
def update(reqeust,id):
    obj=employee.objects.get(id=id)
    if reqeust.method=="POST":
        myform=employeeform(reqeust.POST,instance=obj)
        if myform.is_valid():
            myform.save()
            return redirect('read')
        return redirect('create')
    else:
        myform=employeeform
        return render(reqeust,'update.html',{'form':myform})
def delete(reqeust,id):
    obj = employee.objects.get(id=id)
    if reqeust.method == "POST":
        obj.delete()
        return redirect('read')
    return render(reqeust,'delete.html')


# Create your views here.
