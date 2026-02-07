from django.db import models

# Create your models here.

# this is my table
class Message(models.Model):
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text
    # this method is used to return the string representation of the object. in this case we are returning the text field of the object. 
