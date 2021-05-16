from django.urls import path
from .views import *

app_name = "myapp"
urlpatterns = [
      path("", HomeView.as_view(), name="home"),
      path("register/", CustomerRegistrationView.as_view(), name="customerregistration"),
      path("logout/", CustomerLogoutView.as_view(),name = "customerlogout"),
      path("login/", CustomerLoginView.as_view(),name = "customerlogin"),
      path("profile/", CustomerProfileView.as_view(), name="customerprofile"),
      path("promotion/", PromotionView.as_view(), name="promotion"),
      path("service/",ServiceView.as_view(), name="service"),
      path("mybook/", MybookView.as_view(), name="mybook"),
      path("text/", TextView.as_view(), name="text"),
      path("notifications/", NotificationsView.as_view(), name="notifications"),
      path("customerrate/", CustomerRateView.as_view(), name="customerrate"),
      path("accept/", AcceptView.as_view(), name="accept"),
      path("payment/", PaymentView.as_view(), name="payment"),
      path("booking/", BookingView.as_view(), name="booking"),

      
      ]