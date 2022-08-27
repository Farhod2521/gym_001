from distutils.log import error
import errno
from django.urls import path


from  .views import CustomersDetail, home,customers_table, customer_form_views, customers_edit, CustomerUpdate, CustomersDeleteView

from .signup import Signup
from .login import Login, logout
from .middlewares.auth import auth_middleware 

urlpatterns  = [
    path('', auth_middleware(home), name ="home"),
    path('table/', auth_middleware(customers_table), name="customers_table"),
    path('customer_add/',customer_form_views , name="customer_add"),
    path('customers_edit/<int:pk>/', CustomerUpdate.as_view(), name="edit"),
    path("customer_detail/<int:pk>/", CustomersDetail.as_view(), name="customers_detail"),
    path("customers_delete/<int:pk>/", CustomersDeleteView.as_view(), name="customers_delete"),
    path("signup/", Signup.as_view(), name = "register"),
    path("login/", Login.as_view(), name="login"),
    path('logout/', logout, name = "logout")
]
handler404 = 'main.views.error404'