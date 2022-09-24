class InputValidation: 
    '''
    This class is used to validate the input of the user and return a true or false
    when the input is valid or invalid.
    '''

    def __init__(self):
         '''
        The class constructor.
        Args:
            self (InputValidation): an instance of InputValidation.
        '''
    
    def YesNo(self,user_input):
        '''
        The Method that checks if the user input is a yes or no.
        Args:
            self (InputValidation): an instance of InputValidation.
            user_input (string): The user input.
        '''
        if user_input == "Y" or user_input == "y" or user_input == "N" or user_input == "n":
            return True
        else:
            return False

    def Choices(self,user_input,choices):
        '''
        The Method that checks if the user input is a yes or no.
        Args:
            self (InputValidation): an instance of InputValidation.
            user_input (string): The user input.
            choices (list): The list of choices a user can make.
        '''
        if user_input in choices:
            return True
        else:
            return False