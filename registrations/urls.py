from django.urls import path
from . import views

urlpatterns = [
    path('marriage_thanksgiving/', views.marriage, name='marriage_thanksgiving'),
    path('registration_homepage/', views.registrations_homepage, name='registration'),
    path('birth_notification/', views.birth, name='birth_notification'),
    path('child_dedication/', views.child, name='child_dedication')
]
