from django.shortcuts import render, redirect
import hashlib

from .models import userdata,carousel_Image,guess
from .forms import LoginForm,SignupForm

# A VIEW TO DISPLAY THE FORM REQUIRED TO LOGIN
def form_to_login(request):
    if request.session.has_key('username'):
        username = request.session['username']
        return redirect(login)
    else:
        return render(request, 'login.html', {'text':''})

# A VIEW TO CHECK LOGIN CREDENTIALS OF THE USER
# IF SESSION IS EXISTING, THEN IT WILL SHOW HOME PAGE

def login(request):
    if request.session.has_key('username'):
        username = request.session['username']
        dbusername=userdata.objects.filter(username=username)
        if dbusername:
            list=userdata.objects.all()
        images=carousel_Image.objects.all()    
        return render(request, 'loggedin.html', {"username" : username,'images':images})
    else:
        username=""
        if request.method == "POST":
            MyLoginForm = LoginForm(request.POST)
            if MyLoginForm.is_valid():
                username = MyLoginForm.cleaned_data['username']
                password=MyLoginForm.cleaned_data['password']
                password=hashlib.md5(password.encode())
                password=password.hexdigest()
                dbusername = userdata.objects.filter(username = username)
                dbpassword = userdata.objects.filter(password = password)
                if not dbpassword:
                    if not dbusername:
                        return render(request, 'login.html', {'text':'ENTER CORRECT DETAILS'})
                    else:
                        return render(request, 'login.html', {'text':'ENTER CORRECT PASSWORD'})
                if not dbusername:
                    return render(request, 'login.html', {'text':'ENTER CORRECT DETAILS'})
                request.session['username'] = username
            else:
                MyLoginForm = LoginForm()
    if not username:
        return redirect(form_to_login)
    images=[]
    images=carousel_Image.objects.all()
    return render(request,'loggedin.html',{'username':username,'images':images})
   
# A VIEW TO LOGOUT THE USER

def logout(request):
    try:
       del request.session['username']
    except:
       pass
    return redirect('/')

# A VIEW TO DISPLAY THE SIGNUP PAGE
# IT WILL THEN REDIRECT TO HOME PAGE

def signup(request):
    if request.method=='POST':
        email_f=request.POST.get('email')
        username_f=request.POST.get('username')
        password_f=request.POST.get('password')
        password_f=hashlib.md5(password_f.encode())
        password_f=password_f.hexdigest()
        dbusername = userdata.objects.filter(username = username_f)
        dbemail=userdata.objects.filter(email = email_f)
        if dbemail :
            text="this email is existing."
            return render(request,'signup.html',{'text':text})
        if dbusername:
            text="this username is existing."
            return render(request,'signup.html',{'text':text})
        new_obj=userdata(email=email_f,username=username_f,password=password_f)
        new_obj.save()
        request.session['username'] = username_f
        return redirect(login)
    else:
    	return render(request,'signup.html',{'text':""})

def post(request):
    username=request.session['username']
    return render(request,'upload-pic.html',{'username':username})

def postpic(request):
    username=request.session['username']
    if request.method=='POST':
        name=request.POST.get("namegiven")
        file=request.FILES.get("fileuploaded")
        img_obj=carousel_Image(username=username,name=name,image=file)
        img_obj.save()
    return render(request,'upload-pic.html',{'username':username})

def guessed(request):
    username=request.session['username']
    if request.method=='POST':
        i=1
        while i<carousel_Image.objects.count():
            if request.POST.get(str(i)):
                obj=guess(username=username,guess=request.POST.get(str(i)),num=i)
                obj.save()
            i+=1
    images=[]
    images=carousel_Image.objects.all()
    return render(request,'loggedin.html',{'username':username,'images':images})