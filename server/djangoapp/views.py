from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
import logging

logger = logging.getLogger(__name__)

def about(request):
    return render(request, 'djangoapp/about.html')

def contact(request):
    return render(request, 'djangoapp/contact.html')

def registration_request(request):
    if request.method == 'GET':
        return render(request, 'djangoapp/registration.html')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']

        user_exist = False
        try:
            User.objects.get(username=username)
            user_exist = True
        except User.DoesNotExist:
            logger.debug("New user")

        if not user_exist:
            user = User.objects.create_user(
                username=username,
                password=password,
                first_name=first_name,
                last_name=last_name,
                email=email
            )
            login(request, user)
            return render(request, 'djangoapp/index.html')
        else:
            return render(request, 'djangoapp/registration.html', {'message': "User already exists."})

def login_request(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return render(request, 'djangoapp/index.html', {'user': user})
        else:
            return render(request, 'djangoapp/index.html', {'message': "Invalid username or password."})
    else:
        return render(request, 'djangoapp/index.html')
