# from django.shortcuts import render

# from django.views import View
# another way to import view class is from django.views.generic import View
# from django.views.generic import TemplateView

from django.views.generic import ListView
# ListView helps us to read data from the database and display it in the template.

from .models import Message
# this is function based view

# def messageView(request):
#     return render(request, 'home.html')

# using class based view instead of function based view in order to use this concept in big projects.
# class MessageView(View):
#     def get(self, request):
#         return render(request , 'home.html')

# insteade the above calss view type we use this 
# class MessageView(TemplateView):
class MessageView(ListView):
    model = Message
    template_name = 'home.html'
# model = Message: this tells as to which model we want to read data from the database. in this case we want to read data from the Message model. and it will automatically create a context variable named object_list that contains all the objects of the Message model. and we can use this context variable in our template to display the data. 


