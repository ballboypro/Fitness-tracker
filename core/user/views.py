import datetime
from django.utils import timezone
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from .forms import *

@login_required
def user_page(request):
    BMR = 0.0
    today = timezone.now().date()
    user = request.user
    user_age=today.year - (user.born_date.year) - ((today.month, today.day) < (user.born_date.month, user.born_date.day))
    if user.gender == 'female':
        BMR =  447.6 + (9.2 * user.weight) + (3.1 * user.height) - (4.3 * user_age)
        # print(str(datetime.date.today() - user.born_date))
    else:
        BMR = 88.36 + (13.4 * user.weight) + (4.8 * user.height) - (5.7 * user_age)
    context={'BMR':round(BMR, 2)}
    if request.method == "POST":
        selected_activity = request.POST.get('ActivityRadio')
        calories = BMR * float(selected_activity) - 600
        context={'BMR':round(BMR, 2), 'calories':calories}
        return render(request, 'user/user_page.html',context)
    return render(request, 'user/user_page.html',context)

def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('user:user_page')
    else:
        form = RegistrationForm()
    return render(request, 'user/registration.html', {'form': form})



class UserLoginView(LoginView):
    template_name = 'user/login.html'
    authentication_form = LoginForm

    def get_success_url(self):
        return reverse_lazy('user:user_page') 
    