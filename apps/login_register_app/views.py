# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import User
import bcrypt

def flashErrors(request, errors):
    for error in errors:
        messages.error(request, error)

def index(request):
    return render(request, 'login_register/index.html')

def register(request):
    if request.method == 'POST':
        errors = User.objects.validateRegistration(request.POST)

        if not errors:
            user = User.objects.createUser(request.POST)

            request.session['user_id'] = user.id

            return redirect('/friends')

        flashErrors(request, errors)

    return redirect(reverse('landing'))

def login(request):
    if request.method == 'POST':
        errors = User.objects.validateLogin(request.POST)

        if not errors:
            user = User.objects.filter(email = request.POST['email'])[0]
            print user

            if user:
                password = str(request.POST['password'])
                user_password = str(user.password)
                hashed_pw = bcrypt.hashpw(password, user_password)


                if hashed_pw == user_password:
                    request.session['user_id'] = user.id
                    return redirect('/friends')

            errors.append('Invalid Account Information')

        flashErrors(request, errors)

        print errors
    return redirect(reverse('landing'))


def logout(request):
    if 'user_id' in request.session:
        request.session.pop('user_id')
    return redirect(reverse('landing'))
