from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from django.contrib.auth import authenticate,login,logout
from blloon.forms import OffersForm, RegisterForm

from blloon.models import  BlogModel


class LoginView(auth_views.LoginView):
    template_name = 'pages/login.html'
    def post(self, request, *args, **kwargs):
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)    
        if user is not None:
            login(request,user)
            return redirect('offers')
        else:
            return render(request,'pages/login.html',{'errEmail':"invaild username or password" })
       
def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            new_user=form.save(commit=False)
            new_user.username=None
            new_user.email=username
            new_user.set_password(form.cleaned_data['password1'])
            new_user.is_staff = True
            new_user.save()
            return redirect('pages/login')
          
        else:
            return render(request, 'pages/singup.html', {'form':form})
            
            
    else:
        form = RegisterForm()
    return render(request, 'pages/singup.html', {'form':form})
   
def ForgetPassword(request):
    return render(request, "pages/ForgetPassword.html")

class HomePageView(TemplateView):
    template_name = "pages/home.html"

# class ChefsPageView(TemplateView):  # new
#     template_name = "pages/offers.html"

class ContentPageView(TemplateView):  # new
    template_name = "pages/contact.html"

class BlogPageView(TemplateView):  # new
    template_name = "pages/blog.html"
    
def offers(request):
    post=BlogModel.objects.all()
    print("ksdhkslh")
    return render(request,"pages/offers.html",{"post":post})

def show(request):
    post=BlogModel.objects.all()
    print("ksdhkslh")
    return render(request,"pages/show.html",{"post":post})

def index(request):
    return render(request,'index.html')
 
def create(request):
    if request.method=="POST":
        title=request.POST['title']
        describe_short=request.POST['describe_short']
        describe_long=request.POST['describe_long']
        obj=BlogModel.objects.create(title=title,describe_short=describe_short,describe_long=describe_long)
        obj.save()
        return redirect('/')
    
def destroy(request, id):  
    blog = BlogModel.objects.get(id=id)  
    blog.delete()  
    return redirect("/show")

def edit(request, id):  
    offer = BlogModel.objects.get(id=id)  
    return render(request,'pages/edit.html', {'offer':offer})  

def update(request, id):  
    offer = BlogModel.objects.get(id=id)  
    form = OffersForm(request.POST, instance = offer)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  