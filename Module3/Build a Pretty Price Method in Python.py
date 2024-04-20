"""
In this python coding exercise, we're going to build out a pretty price function.
And so what I mean by pretty price is I mean something that has a normalized price for say an e-commerce shop.
"""


def pretty_price(gross_price, extension):
    if isinstance(extension, int):
        extension = extension * 0.01

    return int(gross_price) + extension


print(pretty_price(3.20, 99))
print(pretty_price(3.99, 0.20))
print(pretty_price(3.20, .95))
print(pretty_price(3, 95))
print(pretty_price(3, 2))

