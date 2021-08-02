
class Logins :
    """
    class that initiates a new intance of login  details 
      """
    login_list = [] # empty login details list

    def __init__(self,application,username,password):
        """
        features of the login class
        """
        self.application = application
        self.username = username
        self.password = password

    def save_login(self):

        '''
        save_login method saves users login details objects into login_list
        '''

        Logins.login_list.append(self)

    def delete_login(self):

        '''
        save_login method deletes users login details objects from login_list
        '''

        Logins.login_list.remove(self)

    @classmethod
    def find_by_app(cls,application):
        '''
        Method that takes in a string and returns login details that matches that application.

        Args:
            number: Phone number to search for
        Returns :
            Contact of person that matches the number.
        '''

        for login in cls.login_list:
            if login.application == string:
                return login
    @classmethod
    def login_exist(cls,application):
        '''
        Method that checks if login details exists from the login list.
        Args:
            number: Application to search if the login details exists
        Returns :
            Boolean: True or false depending if the logins exists
        '''
        for login in cls.login_list:
            if login.application == string:
                    return True

        return False
    @classmethod
    def display_logins(cls):
        '''
        method that returns the login list
        '''
        return cls.login_list