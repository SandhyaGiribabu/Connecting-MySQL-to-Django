from django.shortcuts import render, redirect
from login.models import EmpInsert
from django.contrib import messages
from django.http import HttpResponse

def Insertrecord(request):
    if request.method == 'POST':
        empname = request.POST.get("empname")
        email = request.POST.get("email")
        country = request.POST.get("country")

        # Check if the record already exists in the database
        if not EmpInsert.objects.filter(empname=empname, email=email, country=country).exists():
            saverecord = EmpInsert()
            saverecord.empname = empname
            saverecord.country = country
            saverecord.save()
            messages.success(request, "Record saved successfully!")
        else:
            messages.error(request, "Record already exists!")

        return redirect('welcome_page')
    else:
        return render(request, "Index.html")

def welcome_page(request):
    return render(request, "welcome.html")