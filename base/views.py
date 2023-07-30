from django.shortcuts import render
from .models import Room

# Create your views here.

# rooms = [
#     {'id':1, 'name': 'Lets learn python'},
#     {'id':2, 'name': 'Design'},
#     {'id':3, 'name': 'Frontend developers'},
# ]

# with context we can conditionally pass diff contexts
def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

# without context
# def home(request):
#     return render(request, 'home.html', {'rooms':rooms})

def room(request, pk): # pk primary key
    room = Room.objects.get(id=pk) #get one single item
    context = {'room':room}
    return render(request,'base/room.html', context)

# def room(request, pk):
#     return render(request,'base/room.html')

# now you can add into your pages some like 
# <a href="/room/{{room.id}}">{{room.name}}</a>


'''
after you have a model in the database

- first import the model
'''