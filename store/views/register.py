from django.shortcuts import render , redirect
from django.views import View
from store.models.register import Register
from django.contrib.auth.hashers import make_password

class Registe(View):
    def get(self,request):
        return render(request,'register.html')
    def post(self,request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
         
        value  = {
            'name':name,
            'email':email,
            'password':password,
            'phone':phone
        }
        
        error = None
        if not name:
            error = "Required name.."
        elif len(name) < 4:
            error = "required length name.."
        elif not email:
            error = "Required email.."
        elif not password:
            error = "Required password.."
        elif not phone:
            error = "Required phone.."
        elif Register.isExists(email):
            error="Email already exists.."

        registers = Register(name=name,email=email,password=password,phone=phone)
        if not error:
            registers.password =  make_password(password)
            registers.save()
            return redirect('/login/')
        else:
            data = {
                'error':error,
                'value':value,
            }
        return render(request,'register.html',data)
        
