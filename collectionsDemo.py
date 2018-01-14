import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck(object):
    """

    """
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def getRandomCard(self):
        return choice(self._cards)

    def get4Card(self):
        card1 = list()
        for i in range(13):
            card1.append(self.getRandomCard())
            self._cards.pop(self._cards.index(card1[-1]))
        return card1


class OutCard(object):
    """
    出牌类
    """
    def outFourCard(self, card):
        """
        出4张一样的牌
        """
        pass

    def outTwoCard(self, card):
        """
        出两张一样的牌
        """
        pass

    def outThreeCard(self, card):
        """
        出三张一样的牌
        """
        pass

    def outOneCard(self, card):
        """
        出一张牌
        """
        pass
