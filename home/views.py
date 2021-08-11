from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from accounts.models import Feedback,Post
# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
   
    return render(request, 'index.html')
def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            messages.info(request,username)
            return redirect('/')
        else:
            if ((request.POST.get('username')=="") or (request.POST.get('password')=="")):
                messages.info(request,"Fill Everything!")
                return render(request, 'login.html')


            if request.user.is_anonymous:
                messages.info(request,"Not A User!")
                return redirect("/login")

    
    return render(request, 'login.html')




def logoutUser(request):
    logout(request)
    return redirect("/login")




def coding(request):
    if request.user.is_anonymous:
        return redirect("/login")
        
    return render(request,'coding.html')
def nature(request):
    if request.user.is_anonymous:
        return redirect("/login")
        
    return render(request,'nature.html')
def travel(request):
    if request.user.is_anonymous:
        return redirect("/login")
        
    return render(request,'travel.html')
def feedback(request):
    if request.user.is_anonymous:
        return redirect("/login")
        
    if request.method=="POST":
        Uname = request.POST['Uname']
        Ucontent = request.POST['content']
        print("\n\n",Uname,Ucontent)
        feedback = Feedback(Uname=Uname,feedback=Ucontent)
        feedback.save()
        
    return render(request, 'index.html')

def create(request):
    if request.user.is_anonymous:
        return redirect("/login")
    if request.method=="POST":
        heading = request.POST['heading']
        content = request.POST['content']
        print(heading,content)
        post = Post(heading=heading,content=content)
        post.save()
    return render(request, 'create.html')