from django.shortcuts import render,redirect
from .models import User
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def login_view(request):
    username=request.POST.get('username')
    password=request.POST.get('password')
    email= request.POST.get('email')
    print(username,password,email)
    user=User.objects.filter(username=username,
                             password=password,
                             email=email
                             ).first()
    if user is not None:
        print("user found")
        return redirect("/")
    else:
        print("user not found")
    return render(request, 'login.html')

@csrf_exempt
def signup_view(request):
    if request.method == "POST":
        username = request.POST.get('name')
        password = request.POST.get('password')
        email = request.POST.get('email')
        # Create a new user object with the form data
        user = User.objects.create(
            username=username,
            password=password,
            email=email
        )
        user.save()
    return redirect("/")
def home(req):
    return render(req,'home.html')
