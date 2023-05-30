from django.urls import path
from .views import *
urlpatterns = [
    path('',HomeView,name = 'home-page'),
    path('sargyt/<str:petname>/',SargytView,name = 'sargyt-page'),
    path('dog/',DogView,name = 'dog-page'),
    path('cat/',CatView,name = 'cat-page'),
    path('fish/',FishView,name = 'fish-page'),
    path('hamster/',HamsterView,name = 'hamster-page'),
    path('bird/',BirdView,name = 'bird-page'),
    path('rabbit/',RabbitView,name = 'rabbit-page'),

]
