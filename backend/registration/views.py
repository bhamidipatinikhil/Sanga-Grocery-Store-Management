from django.shortcuts import render
from registration.models import User

# Create your views here.

def register(request):
    if request.method=="POST":
        first_name = request.POST.get('First Name')
        last_name = request.POST.get('Last Name')
        email= request.POST.get('Email ID')
        password = request.POST.get('Password')
        user = User(first_name = first_name, last_name=last_name, email=email, password=password)
        user.save()
    # with open("RegistrationData.txt", "a") as f:
    #     for k, v in request.GET.items():
    #         f.write(str(v))
    # print(type(request.GET["First Name"]))
    return render(request, 'registration/RegistrationPage.html')








