from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View

from .forms import AccountForm
# Create your views here.

class MyAccountView(View):
    form_class = AccountForm()
    # intial = {'key': 'value'}
    template_name = 'account/register.html'
    
    def get(self, request):
        form  = self.form_class
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        if request.method == 'POST':
            form = AccountForm(request.POST)
            if form.is_valid():
                form = form.cleaned_data
                form.save()
                return redirect('account/login')
        return render(request, self.template_name, {'form': form})


class LoginView(View):
    form_class = AccountForm()
    template_name = 'account/login.html'

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})