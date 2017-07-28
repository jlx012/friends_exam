# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, reverse
from ..login_register_app.models import User

def index(request):
    if 'user_id' in request.session:
        current_user = User.objects.currentUser(request)
        friends = current_user.friends.exclude(id=current_user.id)
        users = User.objects.exclude(id__in=friends).exclude(id=current_user.id)

        context = {
            'first_name': current_user.first_name,
            'friends': friends,
            'users': users,
        }
        return render(request, 'friends/index.html', context)

    return redirect(reverse('landing'))

def person(request, id):
    person = User.objects.filter(id=id).first()

    context = {
        'first_name': person.first_name,
        'last_name': person.last_name,
        'email': person.email,
    }

    return render(request, 'friends/person.html', context)

def addFriend(request, id):
    if 'user_id' in request.session:
        current_user = User.objects.currentUser(request)
        friend = User.objects.get(id=id)

        current_user.friends.add(friend)

        return redirect('/friends')

    return redirect('/friends')

def removeFriend(request, id):
    if 'user_id' in request.session:
        current_user = User.objects.currentUser(request)
        friend = User.objects.get(id=id)

        current_user.friends.remove(friend)

        return redirect('/friends')

    return redirect('/friends')
