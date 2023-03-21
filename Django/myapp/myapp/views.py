from django.http import HttpResponse
from django.shortcuts import render
import datetime

def home(request):
    isActive = True
    if request.method=='POST':
        check = request.POST.get("check")
        print(check)
        if check is None: isActive = False
        else: isActive = True



    date = datetime.datetime.now()
    name = "SRHridoy"
    list_of_programs = [
        'Write a program to check even or odd.',
        'Write a program to check vowel or consonant.',
        'Write a program to check GPA grade of a student.'
    ]
    student={
        'student_name':"Hridoy",
        'student_university':"HSTU",
        'student_city':"Rajshahi"
    }

    print("Test Function is called from view")
    #return HttpResponse("<h1>Hello this is index page. </h>" +str(date))
    data={
        'date':date,
        'isActive':isActive,
        'name':name,
        'list_of_programs':list_of_programs,
        'student_data':student
    }
    return render(request,"home.html",data)

def about(request):
    #return HttpResponse("<h1> This is about page</h1>")
    return render(request,"about.html",{})

def services(request):
    #return HttpResponse("<h1> This is Services page</h1>")
    return render(request,"services.html",{})