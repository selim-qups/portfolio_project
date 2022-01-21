#login functionnality
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate, get_user_model
from second_app.forms import *
from django.contrib import messages
#email
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
#user model
UserModel = get_user_model()

#password reset
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
# Create your views here.
def index(request):
    slider = HomePageTopSlider.objects.all()
    home_page_get = HomePageYouGet.objects.all()
    we_complete = HomePageWeComplete.objects.all()
    achivement = Achievement.objects.all()
    context = {
        'slider':slider,
        'home_page_get':home_page_get,
        'we_complete':we_complete,
        'achivement':achivement,

    }
    return render(request, 'second_app/index.html', context)

def sign_up(request):
    registered = False
    if request.method == 'POST':
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active=False
            user.save()
            user_profile = Profile(user=user)
            user_profile.save()
            current_site = get_current_site(request)
            email_sub = 'Account Created Successfully!'
            message = render_to_string('first_app/email.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': default_token_generator.make_token(user),
            })
            send_mail = form.cleaned_data.get('email')
            email = EmailMessage(email_sub, message, to=[send_mail])
            email.send()
            return render(request, 'first_app/after_signup_activeyouraccount.html')

    else:
        form = SignUpForm()
    dict = {'form':form, 'registered':registered}
    return render(request, 'first_app/signup.html', context=dict)


def test2(request):
    return render(request, 'first_app/password_reset.html')



def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = UserModel._default_manager.get(pk=uid)

    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active=True
        user.save()
        messages.info(request, 'Your account hass been activate now!')

        return redirect('login')
    else:
        messages.warning(request, '')

        return HttpResponse('activation code is incorrect!')


def user_login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method == 'POST':
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('dashboard')
        else:
            form = AuthenticationForm()

    context = {'form': form}
    return render(request, 'first_app/login.html', context)


from django.contrib.auth.decorators import login_required
@login_required
def user_logout(request):
    logout(request)
    return redirect('login')


#Client side functionality

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from .models import *

def service(request):
    product = Product.objects.all()
    context = {
        'product': product,
    }
    return render(request, 'second_app/service.html', context)

def our_work(request):
    work = OurWork.objects.all()
    work_list = WorkList.objects.all()

    return render(request, 'second_app/work.html', {'work_list':work_list, 'work': work, })


def team_member(request):
    members = TeamMember.objects.all()
    context = {
        'members':members
    }
    return render(request,'second_app/team_member.html',context)


def about_us(request):
    obj = AboutUs.objects.last()
    return render(request,'second_app/about_us.html',{'obj':obj})
