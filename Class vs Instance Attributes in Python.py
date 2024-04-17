"""
Class vs Instance Attributes in Python
Python'da Sınıf ve Örnek Nitelikleri

Throughout this section on object-oriented programming in Python, we've been working with attributes in relation to
classes quite a bit. But for the most part everything that we've done has been related to instance attributes.
Guide Tasks

What I mean by that is if I were to create a class here and I'll call it class website.
And inside of here, I'm going to have a Dunder init constructor. So say init and then this is going to
receive self and it's also going to receive the title of the website inside of here. I'm going to set
this attributes value or I should say this instance attributes value to self.title and set this equal to
whatever title that gets passed in.
"""


class Website:
    def __init__(self, title):
        self.title = title


ws = Website('My Website Title')
print(ws.__dict__)

ws_two = Website('My Second Title')
print(ws_two.__dict__)


class DifferentWebsite:
    title = 'My Class Title'


dw = DifferentWebsite()
print(dw.title)

dw_two = DifferentWebsite()
print(dw_two.title)
