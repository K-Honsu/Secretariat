from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path('', views.getRoutes),
    path('check/', views.getChildRegistrations),
    path('check/<str:pk>/', views.getChildRegistration),
    path('birth_notification/', views.getBirthNotifications),
    path('birth_notification/<str:pk>/', views.getBirthNotification),
    path('marriage/', views.getMarriageThanksgivings),
    path('marriage/<str:pk>/', views.getMarriageThanksgiving),
]
