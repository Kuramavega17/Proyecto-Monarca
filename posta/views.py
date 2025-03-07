from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db import IntegrityError
from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.urls import reverse
import json
from .models import *

def index(request):

    # Authenticated users view their inbox
    if request.user.is_authenticated:
        return render(request, "posta/index.html")

    # Everyone else is prompted to sign in
    else:
        return HttpResponseRedirect(reverse("login"))
    
def login_view(request):
    
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "posta/login.html", {
                "message": "Invalid email and/or password."
            })
    else:
        return render(request, "posta/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation  :

            print ("Error")
            return render(request, "posta/login.html", {
                "alerta": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, '', password)
            user.save()
        except IntegrityError as e:
            print(e)
            return render(request, "posta/login.html", {
                "alerta": "username address already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "posta/login.html")

# Create your views here.
