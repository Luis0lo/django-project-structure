from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('room/<str:pk>/', views.room, name='room'),
]

'''
by adding name (name='room') and referencing as per the example in home.html
you can now change the name of the path without having to manually change on your pages
path('room/<str:pk>/' = path('department/<str:pk>/'
no implications at all
<a href="{% url 'room' room.id %}">
'''

'''
'room/<str:pk>/' dynamic root accepts a string as primary key (pk)
now in your views.py you have access to pk
'''


# urlpatterns = [
#     path('', views.home, name='home'),
#     path('room/', views.room, name='room'),
# ]
