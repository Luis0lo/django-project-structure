# Register your models here.
from django.contrib import admin

from .models import Room, Topic, Message

admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)

'''
This is so you can see in your admin panel the table you have created
'''