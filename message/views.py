from django.shortcuts import render

# from django.views import View
# another way to import view class is from django.views.generic import View
from django.views.generic import TemplateView

# this is function based view

# def messageView(request):
#     return render(request, 'home.html')

# using class based view instead of function based view in order to use this concept in big projects.
# class MessageView(View):
#     def get(self, request):
#         return render(request , 'home.html')

# insteade the above calss view type we use this 
class MessageView(TemplateView):
    template_name = 'home.html'
