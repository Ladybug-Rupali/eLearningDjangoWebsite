from django.shortcuts import render, redirect
from django.contrib import messages
from eLearnaApp.models import *
from django.http import HttpResponse
from .forms import NewsletterSubscriptionForm


# Create your views here.

def view_base(request):
    resp = render(request,'eLeranaApp/base.html')
    return resp


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

def view_thanks(request):
    resp = render(request,'eLearnaApp/newletterthanks.html')
    return resp

def subscribe_newsletter(request):
    if request.method == 'POST':
        form = NewsletterSubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            resp = render(request,'eLearnaApp/newletterthanks.html')
            return resp
           
        else:
            form = NewsletterSubscriptionForm()
            return render(request, 'eLearnaApp/index.html',{'form':form})




