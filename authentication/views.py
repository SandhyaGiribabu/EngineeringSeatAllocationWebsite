from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import EmailMessage, send_mail
from pythonpro import settings
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth import authenticate, login, logout
from . tokens import generate_token
# from django.contrib.sites.shortcuts import get_current_site
# from django.template.loader import render_to_string
# from django.utils.http import urlsafe_base64_encode
# from django.utils.encoding import force_bytes, force_text
# from . tokens import generate_token

# Create your views here
def index(request):
    return render(request, "authentication/index.html")

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        print(username)
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error(request, "Username already exists! Please try some other username ")

        if User.objects.filter(email=email):
            messages.error(request, "Email already registered!")
            return redirect('home')
        
        if len(username)>10:
            messages.error(request, "Username must be under 10 characters ")

        if pass1 != pass2:
            messages.error(request, "Passwords don't match!")

        if not username.isalnum():
            messages.error(request,"Username must be Alpha-Numeric!" )
            return redirect('home')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.is_active = False
        myuser.save()

        messages.success(request, "Your Account has been successfully created. We have sent you a confirmation email\nPlease confirm your email to activate your account")

        #Email Address Confirmation Email
        current_site = get_current_site(request)
        email_subject = "Confirm your email - TNEA login!!"
        message2 = render_to_string('email_confirmation.html', {
            'name': myuser.first_name,
            'domain' : current_site.domain, 
            'uid' : urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token' : generate_token.make_token(myuser)

        })
        email = EmailMessage(
            email_subject, 
            message2,
            settings.EMAIL_HOST_USER,
            [myuser.email],
        )
        email.fail_silently = True
        email.send()
        # Email Address Confirmation Email 

    return render(request, "authentication/signup.html")


def activate(request,uidb64,token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except (TypeError,ValueError,OverflowError,User.DoesNotExist):
        myuser = None

    if myuser is not None and generate_token.check_token(myuser,token):
        myuser.is_active = True
        # user.profile.signup_confirmation = True
        myuser.save()
        login(request,myuser)
        messages.success(request, "Your Account has been activated!!")
        return render(request, "home.html")
    else:
        return render(request,'activation_failed.html')
    
def signin(request):

        if request.method == "POST":
            username = request.POST['username']
            pass1 = request.POST['pass1']

            user = authenticate(username=username, password=pass1)

            if user is not None:
                login(request, user)
                fname = user.first_name
                return redirect("home")
            
            else:
                messages.error(request, "Wrong Credentials")
                return redirect("index")
            
        return render(request, "authentication/signin.html")
    
def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully")
    return redirect('index')


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def faqs(request):
    return render(request, 'faqs.html')

def contact(request):
    return render(request, 'contact.html')

def registration(request):
    return render(request, 'registration.html')

def choice(request):
    return render(request, 'choice.html')

def seat(request):
    return render(request, 'seat.html')

def apply(request):
    return render(request, 'apply.html')

def apply2(request):
    return render(request, 'apply2.html')
    
