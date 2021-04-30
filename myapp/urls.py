from django.urls import path
from . import views

app_name = 'myapp'
urlpatterns = [
    path('about/<slug:title>', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('form/', views.form_view, name='form')
]
