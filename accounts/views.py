from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages
from accounts.models import Feedback
from .forms import *
from django.core.files.storage import FileSystemStorage

from PIL import Image 
import PIL 


# Create your views here.
def register(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        username = request.POST["username"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]


        if(first_name!="" and last_name!="" and email!="" and username!="" and password1!=""):

            if(password1 == password2 and len(password1)>6):
                if User.objects.filter(username=username).exists():
                    print("Username taken..")
                    messages.info(request, 'Username already taken!')
                    return render(request,"register.html")
                else:
                    user = User.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username, password=password1)
                    user.save()
                    print("User Created")
                    messages.info(request, 'User Created!')
            else:
                print("Password not matching..")
                messages.info(request, 'Password not matching!')
                return render(request,"register.html")
            return redirect("/")
        else:
            messages.info(request, 'Fill Everything!')
            return render(request,"register.html")
    else:
        return render(request,"register.html")



def create(request):

    if request.user.is_anonymous:
        return redirect("/login")
    if request.method=="POST":
        heading = request.POST['heading']
        content = request.POST['content']
        img = '/pics/'+ request.POST['img']
        print(heading,content,img)
        post = Post(heading=heading,content=content,img=img)

        post.save()
 
        return render(request,'index.html')   
    return render(request, 'create.html')









    # if request.method == 'POST':
    #     post = PostForm(request.POST, request.FILES)
  
    #     if post.is_valid():
    #         post.save()
    #         return render(request,'index.html',{'post':post})
    # else:
    #     post = PostForm()
    # return render(request, 'create.html')






