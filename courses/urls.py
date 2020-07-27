from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('who',views.who, name='who'),
    path('course',views.course, name='course'),
    path('terms',views.terms, name='terms'),
    path('register',views.register, name='register'),
    path('registration',views.registration, name='registration'),
    path('enroll',views.enroll, name='enroll'),
    path('enrollment',views.enrollment, name='enrollment')

]