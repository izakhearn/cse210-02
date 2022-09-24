class InputValidation: 
    '''
    This class is used to valdate the input of the user and retrun a true or false.
    '''

    def __init__(self):
        self.input_type = ""
    
    def YesNo(self,user_input):
        if user_input == "Y" or user_input == "y" or user_input == "N" or user_input == "n":
            return True
        else:
            return False

    def Choices(self,user_input,choices):
        if user_input in choices:
            return True
        else:
            return False