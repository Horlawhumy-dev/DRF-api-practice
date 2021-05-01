from django.shortcuts import render,redirect
from django.http import HttpResponse
# from .forms import NewUserForm
from .models import *


# Create your views here.
    

# def base(request):
#     return render(request, 'myapp/base.html', {})

# # Index View herej
# def index_view(request):
#     return render(request, 'myapp/index.html', {})

# # About View here
# def about_view(request, title):
#     name = Something.objects.get(name='Arafat')
#     print(name)
#     context = {'names': name}
#     return render(request, 'myapp/about.html', context)

# # Contact View here
# def contact_view(request):
#      return render(request, 'myapp/contact.html', {})

# def form_view(request):
#     registered = False
#     form = NewUserForm()
#     if request.method == "POST":
#         form = NewUserForm(request.POST)
        
#         # username = request.POST.get('username')
#         # email = request.POST.get('email')
#         # password1 = request.POST.get('password1')
#         # password2 = request.POST.get('password2')
#         if form.is_valid():
#             form.save()
#             registered = True
#             print("User created")
#             redirect("/")
#         else:
#             print("Fill in all fields!")
#     return render(request, 'myapp/form.html', {"form": form, "registered": registered})


