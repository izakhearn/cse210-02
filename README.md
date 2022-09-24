# cse210-02

## HighLow Game

The purpose of this repository is to keep the code for the HighLow game.

The code has the following object and classes

## Input Validation Class

```python
Class       : ValidateInput
File Name   : InputVal.py

**Attributes**
user_input  : string
choices     : list

**Methods**
Choices()   : True or False
YesNo()     : True or False
```

-------

## Card Class

```python
Class       : Card
File Name   : card.py

**Attributes**
    None

**Methods**
random_card : Returns Card value (1-13) and Suite (Spades,Hearts, Diamonds or Clubs)
```

```python
Object      : Current_Card

**Responsibility**
To hold the card that is currently in play

**Behaviors**       **State**
 random_card        Gets a new Random card
```

```python
Object      : New_Card

**Responsibility**
To hold the card that is next in play and use the card to determine if the player was right in choosing High or Low

**Behaviors**       **State**
 random_card        Gets a new Random card
```

-------

## Director Class

```python
Class            : Director
File Name        : director.py

**Attributes**
    None

**Methods**
start_game()     : None 
get_inputs()     : None
do_checkCards()  : None
draw_card_image(): None
```

```python
Object      : Director

**Responsibility**
To hold an instance of the game running and print out the scores and card values it gets from the Card class

**Behaviors**       **State**
 start_game         Starts running the game
 get_inputs         Gets the users inputs
 do_checkCards      Checks if the card was higher or lower 
                    and prints the results
draw_card_image     Draws the appropriate icon for the class 
                    suite
```
