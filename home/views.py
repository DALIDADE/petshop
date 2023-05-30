from django.shortcuts import render,HttpResponse,redirect
from .models import *
from .forms import *

def HomeView(request):
    A = Vip.objects.all()
    return render(request, 'home.html',{'A':A})

def SargytView(request,petname):
    print('Isledi')
    petname=petname
    form = SargytForm()
    if request.method == "POST":
            form = SargytForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.petname = petname
                comment.save()
                return redirect('home-page')

    context = {
               'form':form,
               'petname':petname
    }
    return render(request,'sargyt.html',context)


def DogView(request):
    A = Dog.objects.all()
    return render(request, 'dog.html',{'A':A})


def CatView(request):
    A = Cat.objects.all()
    return render(request, 'cat.html',{'A':A})


def FishView(request):
    A = Fish.objects.all()
    return render(request, 'fish.html',{'A':A})


def HamsterView(request):
    A = Hamster.objects.all()
    return render(request, 'hamster.html',{'A':A})


def BirdView(request):
    A = Bird.objects.all()
    return render(request, 'bird.html',{'A':A})


def RabbitView(request):
    A = Rabbit.objects.all()
    return render(request, 'rabbit.html',{'A':A})

