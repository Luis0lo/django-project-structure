from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    #(null=False) vaoid the table having empty instances
    # participants = 
    updated = models.DateTimeField(auto_now=True)
    #everytime that the save method is called go ahead and print a timestamp
    created = models.DateTimeField(auto_now_add=True)
    # auto_now_add - only takes a snap when we first save or create this instance

    def __str__(self):
        return self.name
    #string reprensetation if the room string(self.name)

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE) 
    #create relationship #cascade to delete all the children messages
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50] # [0:50] cut the messages to 50 char
    
'''
this is where we create our database tables

by creating python classes
every single attribute is represented as a column inside the DB

after adding a model to the databse the first thing to do next is migrations
there is a migrations folder on app

- python manage.py makemigrations and after python manage.py migrate
- this will add a new file on migrations

result : Migrations for 'base':
  base\migrations\0001_initial.py
    - Create model Room

and now the table is oin the database

'''