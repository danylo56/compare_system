from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterFormView.as_view()),
    path('login/', views.LoginFormView.as_view())
]
