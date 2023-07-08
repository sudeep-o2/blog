from django.http import HttpResponse
from django.shortcuts import render,redirect
from . forms import MyUserCreationForm,BlogForm
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from . models import User,Blog
# Create your views here.


def home(request):

    data=Blog.objects.all()

    context={'data':data}
    return render(request,'home.html',context)

def register(request):
    form=MyUserCreationForm()
    if request.method=='POST':
        form=MyUserCreationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.username=user.username.lower()
            user.save()
            login(request,user)
            return redirect('home')

    context={'form':form}
    return render(request,'base/login_reg.html',context)

def loginView(request):
    stat='login'
    if request.method=='POST':
        email=request.POST.get('email').lower()
        password=request.POST.get('password')

        try:
            user=User.objects.get(email=email)
        except:
            return HttpResponse('email does not exist')
        
        user=authenticate(request,email=email,password=password)

        if user is not None :
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse('incorrect password')
        
    context={'stat':stat}
    return render(request,'base/login_reg.html',context)

def logoutView(request):

    logout(request)
    
    return redirect('home')
    
@login_required(login_url='login')
def upload(request):
    form=BlogForm()
    if request.method=='POST':
        Blog.objects.create(
            host=request.user,
            title=request.POST.get('title'),
            description=request.POST.get('description'),
        )
        return redirect('home')

    return render(request,'base/upload.html',{'form':form})

def detailPage(request,pk):
    blog=Blog.objects.get(id=pk)

    context={'blog':blog}
    return render(request,'base/detail.html',context)

@login_required(login_url='login')
def deleteblog(request,pk):
    blog=Blog.objects.get(id=pk)

    if request.user!=blog.host:
        return HttpResponse('you are not allowed to perform the task')

    if request.method=='POST':
        blog.delete()
        return redirect('home')
    
    return render(request,'base/delete.html',{'obj':blog})

@login_required(login_url='login')
def updateblog(request,pk):
    blog=Blog.objects.get(id=pk)
    form=BlogForm(instance=blog)

    if request.user!=blog.host:
        return HttpResponse('you are not allowed to do the task')

    if request.method=='POST':
        blog.title=request.POST.get('title')
        blog.description=request.POST.get('description')

        blog.save()
        return redirect('home')
    
    context={'form':form}

    return render(request,'base/update.html',context)

