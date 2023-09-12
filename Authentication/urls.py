from django.urls import path
from .views import *

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('signup/',SignUpView.as_view()),
    path('enable2FA/',Enable2FA.as_view()),
    path('changepwd/',ChangePWDView.as_view()),
    path('authWindowStyle/',AuthWindowStyleView.as_view())

]