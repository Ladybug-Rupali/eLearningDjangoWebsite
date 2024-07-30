from django.urls import path
from .views import *

urlpatterns = [


    path('index/',view_index,name='index'),
    path('about/',view_about,name='about'),
    path('courses/',view_courses,name='courses'),
    path('contact/',view_contact,name='contact'),
    path('team/',view_team,name='team'),
    path('testimonial/',view_testimonial,name='testimonial'),
    path('404/',view_404,name='404'),
    path('thankyou/',view_404,name='thankyou'),
    path('base/',view_base,name='base'),
    path('newsletter/', subscribe_newsletter, name='newsletter'),
    path('thanks/', view_thanks, name='thanks'),


    
]