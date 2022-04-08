from django.shortcuts import redirect, render
from django.views import View

from store.models.register import Register
from django.contrib.auth.hashers import check_password

class Login(View):
    def get(self,request):
        return render(request,'login.html')
    def post(self,request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Register.get_email_by_id(email)
        if customer:
            flag = check_password(password,customer.password)
            if flag:
                request.session['customer_id'] = customer.id
                request.session['email']=customer.email
                return redirect('home')
            else:
                error="Password invalid.."
        else:
            error="email and password invalid.."
        return render(request,'login.html',{'error':error})
