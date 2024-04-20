"""
In the last guide, we walk through how we could leverage polymorphism in a python program to generate HTML.
And that is going to be a common way that you implement inheritance and polymorphism.

But Python also gives us another option, so right here we were able to create an abstract class and
then have a few classes that inherited from it. But if you do not want to follow this type of pattern we
also have another way of doing this and we're going to leverage functions in order to make it possible.
"""


class Heading:
    def __init__(self, content):
        self.content = content

    def render(self):
        return f'<h1>{self.content}</h1>'


class Div:
    def __init__(self, content):
        self.content = content

    def render(self):
        return f'<div>{self.content}</div>'


div_one = Div('Some content')
heading = Heading('My Amazing Heading')
div_two = Div('Another div')


def html_render(tag_object):
    print(tag_object.render())


html_render(div_one)
html_render(div_two)
html_render(heading)
