from django.urls import path
from .views import *

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('signup/',SignInView.as_view()),
    path('changepwd/',ChangePWDView.as_view()),

]