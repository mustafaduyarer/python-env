"""

So far in this section we've walked through a number of the Dunder methods that are available in python.
In this guide, we're going to walk through two very interesting ones and they're going to allow us to build a full
iterable module inside of Python. And if you do not know what iteration is you have been using it ever since you
 learned about loop's so different tools such as lists and dictionaries and tuples those are iterable and as great
  as they are sometimes you may need to implement your own type of iteration and that's all we're going to walk
  through in this guide.
"""


class Lineup:

    def __init__(self, players):
        self.players = players
        self.last_player_index = (len(self.players) - 1)

    def __iter__(self):
        self.n = 0
        return self

    def get_player(self, n):
        return self.players[n]

    def __next__(self):
        if self.n < self.last_player_index:
            player = self.get_player(self.n)
            self.n += 1
            return player
        elif self.n == self.last_player_index:
            player = self.get_player(self.n)
            self.n = 0
            return player


astros = [
    'Springer',
    'Bregman',
    'Altuve',
    'Correa',
    'Reddick',
    'Gonzalez',
    'McCann',
    'Davis',
    'Tucker',
    'Mustafa'
]

astros_lineup = Lineup(astros)
process = iter(astros_lineup)

print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))

