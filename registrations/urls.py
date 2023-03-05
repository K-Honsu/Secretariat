from django.urls import path
from . import views

urlpatterns = [
    path('marriage_thanksgiving/', views.marriage, name='marriage_thanksgiving'),
    path('registration_homepage/', views.registrations_homepage, name='registration'),
    path('birth_notification/', views.birth, name='birth_notification'),
    path('child_dedication/', views.child, name='child_dedication'),
    path('abort/', views.abort, name='abort'),
    path('all_marriage/', views.all_marriage_thanksgiving, name='marriage_thanks'),
    path('all_birth/', views.all_birth_notification, name='all_birth'),
    path('all_child/', views.all_child_dedications, name='all_child'),
]
