from game.card import Card
from lib.input import InputValidation as Validate


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        dice (List[Die]): A list of Die instances.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.card = Card()
        self.is_playing = True
        self.score = 300
        self.total_score = 0
        self.current_card = ''


    def start_game(self):
        """Starts the game loop to control the sequence of play.

        Args:
            self (Director): An instance of Director.
        """
        while self.is_playing:
            self.get_inputs()
            self.do_outputs()
    
    def get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means getting a new card.

        Args:
            self (Director): An instance of Director.
        """
        if self.current_card == '':
            self.current_card = self.card.random_card()
        print (f"\nCurrent card is the {self.current_card[1]} of ", end='')
        self.draw_card_image()
        self.player_input = input("Higher or lower? [h/l] ")
        while Validate.Choices(self,self.player_input,["H", "L","h","l"]) == False:
            print("Wrong Choice. Please try again.")
            self.player_input = input("Higher or lower? [h/l] ")
        self.player_input = self.player_input.lower()
        self.newCard = self.card.random_card()

    
    def do_checkCards(self):
        '''Check if the new card is higher or lower than the current card.'''
        if self.player_input == "h":
            if self.newCard[1] > self.current_card[1]:
                self.score += 100
            else:
                self.score -= 75
        elif self.player_input == "l":
            if self.newCard[1] < self.current_card[1]:
                self.score += 100
            else:
                self.score -= 75
        self.current_card = self.newCard
        if self.score == 0:
            self.is_playing = False

    def draw_card_image(self):
        '''Draw the card image.'''
        if self.current_card[0] == "Hearts":
            print("♥")
        elif self.current_card[0] == "Diamonds":
            print("♦")
        elif self.current_card[0] == "Spades":
            print("♠")
        else:
            print("♣")
    
    def do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means the card and the score.

        Args:
            self (Director): An instance of Director.
        """
        self.do_checkCards()
        print (f"Next card is the {self.newCard[1]} of ", end='')
        self.draw_card_image()
        print(f"Your score is {self.score}.")
        if self.score == 0:
            print("You lose!")
        else:
            self.play_again = input("Keep playing? [y/n] ")
            while Validate.YesNo(self,self.play_again) == False:
                print("Wrong Choice. Please try again.")
                self.play_again = input("Keep playing? [y/n] ")
            self.play_again = self.play_again.lower()
            if self.play_again == "n":
                self.is_playing = False
                print(f"Your final score is {self.score}.")
            else:
                print(f"Your score is now {self.score}.")