from user_credentials import user
from user_credentials import user_credentials

class Password:
    """
    Class that generates new instances of password.
    """
    

    password_locker = [] # Empty password locker
     # Init method up here
    def save_pasword(self):

        '''
        save_pasword method saves pasword objects into pasword_list
        '''

        Pasword.pasword_list.append(self)

    def __init__(self,first_name,last_name,password):

      # docstring removed for simplicity

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
    @classmethod

    def display_user(cls):
        '''
        method that returns the user list
        '''
        return cls.users_list
        