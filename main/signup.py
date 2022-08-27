from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from .models import HodAdmin
from django.views import View



class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        full_name = request.POST.get("full_name")
        phone  =  request.POST.get("phone")
        username = request.POST.get("username")
        password =  request.POST.get("password")


        value = {
            "full_name":full_name,
            "phone":phone,
            "username" : username,
            
        }
        error_message = None
        hodadmin  =  HodAdmin(
            full_name = full_name,
            phone = phone,
            username = username,
            password = password
        )
        error_message = self.validateHodAdmin(hodadmin)
        if not error_message:
            print(full_name, phone, username, password)
            hodadmin.password = make_password(hodadmin.password)
            hodadmin.register()
            return redirect("home")
        else:
            data = {
                'error':error_message,
                "values":value
            }  
            return render(request, 'signup.html', data)

    def validateHodAdmin(self, hodadmin):
        error_message = None
        if (not hodadmin.full_name):
            error_message = "Ism familyangizni kiriting !!!!!!"
        elif len(hodadmin.full_name) < 4:
            error_message = "Ism Familyangizni To'liq kiriting ?"
        elif not hodadmin.phone:
            error_message = "Telfon raqamingizni kiriting !!!!"
        elif len(hodadmin.phone) < 6:
            error_message = "Telfon raqamingizni to'liq kiriting"
        elif not hodadmin.username:
            error_message = "Username kiriting"
        elif len(hodadmin.username) <4 :
            error_message = "Username 4 harfdan ko'proq soz kiriting"
        elif not hodadmin.password:
            error_message = "Parolni kiriting"
        elif len(hodadmin.password) < 6:
            error_message = "Parol belgidan ko'proq qoying"
        
        return error_message
