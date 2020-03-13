from django.shortcuts import render
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login




class LoginFormView(FormView):
    form_class = AuthenticationForm

    template_name = "user_registration/login.html"

    success_url = "/"

    def form_valid(self, form):
        self.user = form.get_user()

        # Выполняем аутентификацию пользователя.
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)

class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = "/user_register/login"
    template_name = "user_registration/register.html"

    def form_valid(self, form):
        form.save()

        return super(RegisterFormView, self).form_valid(form)



# Create your views here.
