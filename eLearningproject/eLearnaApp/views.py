from django.shortcuts import render
from eLearnaApp.models import *
from django.http import HttpResponse
from .forms import EmailInputForm


# Create your views here.


def view_index(request):
    resp = render(request,'eLearnaApp/index.html')
    return resp

def view_about(request):
    resp = render(request,'eLearnaApp/about.html')
    return resp

def view_courses(request):
    resp = render(request,'eLearnaApp/courses.html')
    return resp

def view_team(request):
    resp = render(request,'eLearnaApp/team.html')
    return resp

def view_contact(request):
    if request.method == "GET":
        resp = render(request,'eLearnaApp/contact.html')
        return resp
    elif request.method == "POST":
        if 'btnmsg' in request.POST:
            con = Contact()
            con.name = request.POST.get('name')
            con.email = request.POST.get('email')
            con.subject = request.POST.get('subject')
            con.message = request.POST.get('message')
            con.save()
    resp = render(request,'eLearnaApp/thankyou.html')
    return resp


def view_testimonial(request):
    resp = render(request,'eLearnaApp/testimonial.html')
    return resp

def view_404(request):
    resp = render(request,'eLearnaApp/404.html')
    return resp

def view_thankyou(request):
    resp = render(request,'eLearnaApp/thankyou.html')
    return resp


# def view_email(request):
#     if request.method=="POST":
#         if 'signup' in request.POST:
#             e1 = EmailInput()
#             e1.email = request.POST.get('email1')
#             e1.save()
#     resp = HttpResponse("<h1>Submitted</h1>")
#     return resp


# def email_input_view(request):
#     if request.method == 'POST':
#         if 'signup' in request.POST:
#             form = EmailInputForm(request.POST)
#             if form.is_valid():
#                 form.save()
#                 return HttpResponse("<h1>Submitted</h1>")
#             else:
#                 form = EmailInputForm()

#             # If form is not valid or GET request, render the base template with form
#             return render(request, 'eLearnaApp/contact.html')