from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView, CreateView, FormView
from .forms import  CustomerRegistrationForm, CustomerLoginForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from .models import *


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['myname'] = "Oat chigga"
        return context


class CustomerRegistrationView(CreateView):
    template_name = "customerregistration.html"
    form_class = CustomerRegistrationForm
    success_url = reverse_lazy("myapp:home")

    def form_valid(self, form):
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        email = form.cleaned_data.get("email")
        user = User.objects.create_user(username, email, password)
        form.instance.user = user
        login(self.request, user)
        return super().form_valid(form)

    def get_success_url(self):
        if "next" in self.request.GET:
            next_url = self.request.GET.get("next")
            print(next_url)
            return next_url
        else:
            return self.success_url


class CustomerLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("myapp:home")  

class CustomerLoginView(FormView):
    template_name = "customerlogin.html"
    form_class = CustomerLoginForm
    success_url = reverse_lazy("myapp:home")

    # form_valid method is a type of post method and is available in createview formview and updateview
    def form_valid(self, form):
        uname = form.cleaned_data.get("username")
        pword = form.cleaned_data["password"]
        usr = authenticate(username=uname, password=pword)
        if usr is not None and usr.customer:
            login(self.request, usr)
        else:
            return render(self.request, self.template_name, {"form":self.form_class, "error": "Invalid credentials"})

        return super().form_valid(form)

    def get_success_url(self):
        if "next" in self.request.GET:
            next_url = self.request.GET.get("next")
            print(next_url)
            return next_url
        else:
            return self.success_url


class CustomerProfileView(TemplateView):
    template_name = "customerprofile.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.customer:
            pass
        else:
            return redirect("/login/?next=/profile/")
        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        customer = self.request.user.customer
        context['customer'] = customer
        return context

class PromotionView(TemplateView):
    template_name = "promotion.html"

class ServiceView(TemplateView):
    template_name = "service.html"

class MybookView(TemplateView):
    template_name = "mybook.html"

class TextView(TemplateView):
    template_name = "text.html"

class NotificationsView(TemplateView):
    template_name = "notifications.html"

class CustomerRateView(TemplateView):
    template_name = "customerrate.html"


class AcceptView(TemplateView):
    template_name = "accept.html"


class PaymentView(TemplateView):
    template_name = "payment.html"

class BookingView(TemplateView):
    template_name = "booking.html"