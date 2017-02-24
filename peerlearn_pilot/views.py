from django.shortcuts import render

from django.shortcuts import redirect
from django.core.exceptions import ObjectDoesNotExist

# Decorator to use built-in authentication system
from django.contrib.auth.decorators import login_required

# Used to create and manually log in a user
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

# Django transaction system so we can use @transaction.atomic
from django.db import transaction

# Imports the Item class
from peerlearn_pilot.models import *

from datetime import datetime

# Create your views here.
# Create your views here.


def home(request):

    return render(request, "peerlearn_pilot/welcome.html")

def provide_info(request):
    context = {}
    errors = []
    context['errors'] = errors

    if request.method == 'GET':
        return render(request,"peerlearn_pilot/welcome.html")

    if not 'clarity' in request.POST or not request.POST['clarity']:
        errors.append("Your response on clarity of arguments is required.")
    else:
        context['clarity'] = request.POST['clarity']

    if not 'logic' in request.POST or not request.POST['logic']:
        errors.append("Your response on clarity of arguments is required.")
    else:
        context['logic'] = request.POST['logic']

    if not 'accuracy' in request.POST or not request.POST['accuracy']:
        errors.append("Your response on accuracy and adequacy of arguments is required.")
    else:
        context['accuracy'] = request.POST['accuracy']

    if not 'mturkid' in request.POST or not request.POST['mturkid']:
        errors.append("You need to specify your MturkID.")
    else:
        context['mturkid'] = request.POST['mturkid']

    if errors:
        return render(request,"peerlearn_pilot/welcome.html", context)

    new_learner = Learner(mturkid = request.POST['mturkid'],
                          feedback_clarity  = request.POST['clarity'],
                          feedback_logic = request.POST['logic'],
                          feedback_accuracy = request.POST['accuracy'],
                          )
    new_learner.save()
    context['mturkid'] = request.POST['mturkid']
    return render(request, "peerlearn_pilot/success.html", context)






