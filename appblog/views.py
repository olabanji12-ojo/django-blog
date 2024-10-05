from django.shortcuts import render, redirect
from .models import Person, Message
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from.forms import BlogCreationForm, UserCreationForm, PersonForm, MessageForm
from django.db.models import Q
from django.http import HttpResponse



@login_required(login_url='loginpage')
def home(request):
    # persons = Person.objects.all()
    profiles = Message.objects.all()
    q = request.GET.get('q')
    if q != None:
        persons = Person.objects.filter(name__icontains=q)
    else:
        persons = Person.objects.all()
        
        
        
    context = {'persons': persons, 'profiles' : profiles}
    return render(request, 'home.html', context)


def loginpage(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'username does not exist')
        user = authenticate(request, username=username, password=password )
        if user != None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'username or password does not exist')
            
            
        
    
    context = {}
    return render(request, 'loginpage.html', context)

@login_required(login_url='loginpage')
def logoutpage(request):
    
    logout(request)
    return redirect('loginpage')
    
    context = {}
    return render(request, 'loginpage.html', context)

def registerpage(request):
    form = BlogCreationForm()
    if request.method == 'POST':
        form = BlogCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'an error occured during registeration')
            
    
    context = {'form' : form}
    return render(request, 'registerpage.html', context)


def create_post(request):
    form = PersonForm()
    if request.method == 'POST':
        form = PersonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    context = {'form' : form}
    return render(request, 'create_post.html', context)

def edit_post(request, id):
    persons = Person.objects.get(id=id)
    form = PersonForm(instance=persons)
    if request.method == 'POST':
        form = PersonForm(request.POST, request.FILES, instance=persons)
        if form.is_valid():
            form.save()
            return redirect('home')
            
    
    context = {'form' : form}
    return render(request, 'create_post.html', context)

def delete_post(request, id):
    persons = Person.objects.get(id=id)
    if request.method == 'POST':
        persons.delete()
        return redirect('home')
    
    context = {'obj' : persons}
    return render(request, 'delete_post.html', context)

def profile(request, id):
    persons = Person.objects.get(id=id)
    room_messages = persons.message_set.all().order_by('-created')
    if request.method == 'POST':
       message = Message.objects.create(
           user = request.user,
           bio = request.POST.get('body'),
           person = persons
         
       ) 
       return redirect('profile', id=persons.id)

    context = {'persons' : persons, 'room_messages' : room_messages}
    return render(request, 'profile.html', context)




def delete_message(request, id):
    messages_form = Message.objects.get(id=id)
    if request.method == 'POST':
       messages_form.delete()
       return redirect('home')

    
    context = {'obj' : messages_form}
    return render(request, 'delete_post.html', context)

   

