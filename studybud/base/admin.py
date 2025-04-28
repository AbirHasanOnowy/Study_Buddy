from django.contrib import admin

# Register your models here.

from .models import Room, Topic, Message, User # Import Room, Topic and Message models

admin.site.register(User) # Register User model to admin pannel.
admin.site.register(Room) # Register Room model to admin pannel.
admin.site.register(Topic) # Register Topic model to admin pannel.
admin.site.register(Message) # Register Message model to admin pannel.
