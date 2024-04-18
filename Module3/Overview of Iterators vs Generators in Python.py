
"""

But another option that you will have access to is to build what is called a generator.
And that's what we're going to walk through in this guide. So we're actually going to replicate the exact
same behavior but we're going to use a different tool. And then you're going to be able to see side by side
what those implementations look like so you can see which option you prefer.

So I'm going to quit out of this. And I created a generator file that right now simply has the exact same
list that we were working with before.
"""


class InfiniteLineup:
    def __init__(self, players):
        self.players = players

    def lineup(self):
        lineup_max = len(self.players)
        #print(lineup_max)
        idx = 0

        while True:
            if idx < lineup_max:
                yield self.players[idx]
            else:
                idx = 0
                yield self.players[idx]

            idx += 1

    def __repr__(self):
        return f'InfiniteLineup({self.players})'

    def __str__(self):
        return f"InfiniteLineup with the players: {', '.join(self.players)}"


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

full_lineup = InfiniteLineup(astros)
astros_lineup = full_lineup.lineup()

print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))

print(repr(full_lineup))

print(str(full_lineup))
