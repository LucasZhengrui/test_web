from django.shortcuts import render
import hashlib
import sqlite3
from django.http import HttpResponseRedirect
from .models import user

# Create your views here.

def goto_index_view(request,url):
    # Redirect to appropriate page
    return HttpResponseRedirect(url)

def register(request):
    Error_message = ""
    if request.method == 'POST':
        # get data from request.POST
        User_psd = request.POST.get('Password')
        User_confirm_psd = request.POST.get('Confirm_Password')
        
        if User_psd != User_confirm_psd:
              Error_message = "Oooops, something wrong! Please insert same password twice!"
              return render(request, 'login/signup.html',{'Error_message':Error_message})
        
        Password_md5_signup = hashlib.md5(User_psd.encode('utf-8')).hexdigest()
        name = request.POST.get('name')
        admin = 0

        # create a new user in the database
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO login_user(User_name, User_password, Is_admin) VALUES (?, ?, ?)", (name, Password_md5_signup, admin))
        conn.commit()
        conn.close()

        response = goto_index_view(request,'/')
        return response
    else:
        return render(request, 'login/signup.html')

def login(request):
    if request.method == 'POST':
        # Get the user nickname and password
        Username = request.POST.get('Username')
        Password = request.POST.get('Password')

        # Search user in the database
        try:
            User = user.objects.get(User_name=Username)
        except user.DoesNotExist:
            error_message = 'Bad luck, user is not found!'
            return render(request, 'login/login.html', {'error_message': error_message})

        # Check password, is it correct?
        Password_md5 = hashlib.md5(Password.encode('utf-8')).hexdigest()
        if Password_md5 != User.User_password:
            error_message = 'Password is incorrect!'
            return render(request, 'login/login.html', {'error_message': error_message})

        # Create a response object and set a cookie
        response = goto_index_view(request,'/')
        response.set_cookie('Username', Username)

        return response

    else:
        response = render(request, 'login/login.html')
        Username = request.COOKIES.get('Username')
        try:
            User = user.objects.get(User_name=Username)
        except user.DoesNotExist:
            pass
        
        response.delete_cookie('Username')
        return response