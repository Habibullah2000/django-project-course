# from django.test import TestCase

from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.
class MessagePageTests(SimpleTestCase):
    
    def test_message_page_correct_location(self):
        # first we should send a request to my web server and get a response. and for that we use self.client method
        response = self.client.get("/message/")     
        self.assertEqual(response.status_code, 200)
        # What is asser: assert is a way to check if the output is what we expect it to be. and if the program is not working as expected it will raise an error. Then assertEqual is a method that checks if two values are equal. In this case we are checking if the response status code is 200.

    # secode test checking url.
    def test_url_available_by_name(self):
        response = self.client.get(reverse('message'))
        # what is reverse: reverse is a method that takes the name of the url and returns the url. in this case we are using the name of the url that we defined in urls.py file. and it will return the url that we defined in urls.py file.
        self.assertEqual(response.status_code, 200)

    # third test checking template
    def test_template_name(self):
        response = self.client.get(reverse('message'))
        self.assertTemplateUsed(response, 'home.html')
        # what is assertTemplateUsed: assertTemplateUsed is a method that checks if the template used in the response is the one we expect it to be. in this case we are checking if the template used in the response is home.html. and if it is not home.html it will raise an error.

    # fourth test checking content
    def test_message_content(self):
        response = self.client.get(reverse('message'))
        self.assertContains(response, '<h1>this is your message</h1>')
        # what is assertContains: assertContains is a method that checks if the response contains a certain string. in this case we are checking if the response contains home.html. and if it does not contain home.html it will raise an error.