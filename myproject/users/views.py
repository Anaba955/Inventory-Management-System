from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import requires_csrf_token
from django.views.decorators.csrf import csrf_protect

@requires_csrf_token
def csrf_failure_view(request, reason=""):
    return render(request, 'csrf_failure.html', {'reason': reason})

def csrf_failure_view(request, reason=""):
    return render(request, 'csrf_failure.html')


def signup(request):
    if request.method == 'POST':
        # Retrieve form data
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if not username or not email or not password or not confirm_password :
            messages.error(request, 'Please fill in all the fields.')
            return redirect('signup')
        
         # Check if the username already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Eamil already exists.')
            return redirect('signup')
        
         # Perform password validation
        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return redirect('signup')

        # Create a new User instance
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            # first_name=first_name,
            # last_name=last_name
        )
        
        # Save the user
        user.save()

        # Success message
        messages.success(request, 'Registration successful. You can now login.')
        login(request, user)
        return redirect('index')
    
        # Redirect to the login page
    #     return redirect('login1')

    return render(request, 'users/register.html')
    



def login1(request):
    if request.method == 'POST':
        # Retrieve form data
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # User is valid, log in
            login(request, user)
            return redirect('index')
        else:
            # Invalid login credentials, display error message
            messages.error(request, 'Invalid username or password.')

    return render(request, 'users/login1.html')