from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    # path('signup/', views.signup_view, name='signup'),
    path('doctor-dashboard/', views.doctor_dashboard, name='doctor_dashboard'),
    path('patient-dashboard/', views.patient_dashboard, name='patient_dashboard'),
   path('login/', views.login_view, name='login')
]
