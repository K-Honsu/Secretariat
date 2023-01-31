from django.urls import path
from . import views

urlpatterns = [
    path('marriage_thanksgiving/', views.marriage, name='marriage_thanksgiving')
]
