from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
import uuid

from .forms import CustomUserForm
from .models import CustomUser

# Create your views here.

def register_view(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_email_verified = False
            token = str(uuid.uuid4())
            user.email_verification_token = token

            current_site = get_current_site(request)
            subject = 'Verify your email address'
            from_email = 'info@ishop.com'
            recipient_list = [form.cleaned_data['email'],]
            verification_link = f'http://{current_site}/accounts/verify-email/{token}/'
            message = f'Click the following link to verify your email:\n{verification_link}'

            send_mail(subject, message, from_email, recipient_list,)

            user.save()
            return redirect('accounts:login')

    form = CustomUserForm()
    return render(request, 'accounts/register.html', {'form': form})


def verify_email_view(request, token):
    user = CustomUser.objects.get(email_verification_token=token)
    if user:
        user.is_email_verified = True
        user.email_verification_token = None
        user.save()
        return redirect('accounts:login')


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user.is_email_verified:
                login(request, user)
                return redirect('accounts:register')

    else:
        form = AuthenticationForm()
        return render(request, 'accounts/login.html', {'form': form})

# from django.contrib import messages

# def login_view(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(data=request.POST)
#         try:
#             if form.is_valid():
#                 user = form.get_user()
#                 if user.is_email_verified:
#                     login(request, user)
#                     return redirect('accounts:register')
#                 else:
#                     raise ValueError('Email not verified')
#             else:
#                 raise ValueError('Invalid form data')
#         except ValueError as e:
#             messages.error(request, str(e))

#     else:
#         form = AuthenticationForm()

#     return render(request, 'accounts/login.html', {'form': form})