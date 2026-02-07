from django.contrib import admin

from .models import Message
# by this impot we can see our table in admin panel and we have access to that model in admin panel. 

# Register your models here.
admin.site.register(Message)
# this is the way to register our model in admin panel and we can see our table in admin panel and we have access to that model in admin panel.
