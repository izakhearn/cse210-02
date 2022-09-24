import random

class Card:

    '''
    The card class is responsible for storing the suit and value of a card. 

    Attributes:
        suit (string): The suit of the card.
        value (int): The value of the card.
    '''

    def __init__(self):
        '''
        The class constructor.
        Args:
            self (Card): an instance of Card.
        '''
        self.suit = ""
        self.value = 0

    def random_card(self):
        '''
        The method that generates a random card.
        Args:
            self (Card): an instance of Card.
        '''
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        return (random.choice(suits), random.randint(1, 13))