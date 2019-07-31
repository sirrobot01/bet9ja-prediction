from django.urls import path, include
from . import views
from rest_auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.HomePageViews.as_view()),
    path('view/', views.ViewOdds.as_view()),
    path('signup/', views.UserRegistration.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view())
]