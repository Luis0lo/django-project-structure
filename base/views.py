from django.shortcuts import render

# Create your views here.

rooms = [
    {'id':1, 'name': 'Lets learn python'},
    {'id':2, 'name': 'Design'},
    {'id':3, 'name': 'Frontend developers'},
]

# with context we can conditionally pass diff contexts
def home(request):
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

# without context
# def home(request):
#     return render(request, 'home.html', {'rooms':rooms})

def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {'room':room}
    return render(request,'base/room.html', context)

# def room(request, pk):
#     return render(request,'base/room.html')

# now you can add into your pages some like 
# <a href="/room/{{room.id}}">{{room.name}}</a>