# from datetime import datetime
# from datetime import timedelta

from django.contrib import messages
from django.contrib.auth import update_session_auth_hash, logout
# from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import password_validators_help_text_html as pass_help
# from django.http import Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.utils import timezone

from . import forms
from .utils import send_activation_email
from .models import Profile

"""
Use this to debug
import ipdb; ipdb.set_trace()
"""


def index(request):

    context = {
        'title': "Home Page",
    }
    return render(request, 'accounts/index.html', context)

def register(request):
    if request.user.is_authenticated():
        return redirect('index')
    elif request.method == 'POST':
        form = forms.Register(request.POST)
        if form.is_valid():
            user = form.save()
            send_activation_email(user)
            return redirect(reverse('accounts:register_done'))
        else:
            messages.error(request, "Form did not validate, see errors below.")
    else:
        form = forms.Register()

    context = {
        'title': "Register an Account",
        'form': form,
        'submit': "Register",
        'password_help_text': pass_help(),
    }
    return render(request, 'main/generic_form.html', context)

def register_done(request):
    if request.user.is_authenticated():
        return redirect('index')
    else:
        context = {
            'title': "Register Account Success",
            'message': "Please check your email now for an activation link.",
        }
        return render(request, 'accounts/success_page.html', context)


# View called from activation email. Activate user if link didn't expire (48h default),
# or offer to send a second link if the first expired.
def activation(request, key):
    profile = get_object_or_404(Profile, activation_key=key)
    if profile.user.is_active is False:
        if timezone.now() > profile.key_expires:
            messages.warning(request, "Activation link expired. "
                                      "Please check your email for a new link.")
            user = User.objects.get(id=profile.user.user_id)
            if user is not None:
                send_activation_email(user)
            return redirect('index')
        else:  # Activation successful
            profile.user.is_active = True
            # profile.key_expires = datetime.strftime(datetime.now())
            profile.user.save()
            messages.success(request, "Activation successful, please login.")
            return redirect(reverse('accounts:login'))

    # If user is already active, simply display error message
    else:
        messages.error(request, "User is already activated, please login.")
        return redirect(reverse('accounts:login'))


@login_required
def edit(request):
    if request.method == 'POST':
        form = forms.EditUser(request.POST)
        if form.is_valid(user=request.user):
            data = form.cleaned_data
            user = request.user
            user.first_name = data['first_name']
            user.last_name = data['last_name']
            user.save()
            if data['email'] != "" and data['email'] != user.email:
                user.email = data['email']
                user.is_active = False
                user.save()
                send_activation_email(user)
                logout(request)
                messages.success(request, "Email successfully updated.")
                return redirect(reverse('accounts:register_done'))

            messages.success(request, "User info updated.")
            return redirect(reverse('accounts:profile'))
    else:
        form = forms.EditUser(initial={'first_name': request.user.first_name,
                                       'last_name': request.user.last_name,
                                       'email': request.user.email})

    context = {
        'title': "Edit User Information",
        'form': form,
        'submit': "Edit",
    }
    return render(request, 'main/generic_form.html', context)

@login_required
def profile(request):
    context = {
        'title': "User Profile",
    }
    return render(request, 'accounts/profile.html', context)


@login_required
def change_password(request):
    if request.method == "POST":
        form = forms.ChangePassword(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated.')
            return redirect('accounts:profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = forms.ChangePassword(request.user)

    context = {
        'title': "Change Password",
        'password_help_text': pass_help(),
        'submit_button': "Change Password",
        'form': form,
    }
    return render(request, 'accounts/login.html', context)

