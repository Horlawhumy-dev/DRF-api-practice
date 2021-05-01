from django.urls import path

from .views import MyAccountView, LoginView

app_name = 'account'
urlpatterns = [
    # path('register/', MyAccountView.as_view(), name='my-account-view'),
    # path('login/', LoginView.as_view(), name='login-view')
]
