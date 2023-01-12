import requests


def dict_to_query(dictionary):
    """(dict)->str
    take a dictionnary as a input and return a specific string format
    >>> dict_to_query({'email': 'ruijiameng@mcgill.ca', 'token': 'idk'})
    'email=ruijiameng@mcgill.ca&token=idk'
    >>> dict_to_query({'name': 'ruijiameng', 'class': 'comp202'})
    'name=ruijiameng&class=comp202'
    >>> dict_to_query({'466373': '664747', "343434": 'c33443'})
    '466373=664747&343434=c33443'
    """
    string=""
    for key in dictionary:
        string+=(str(key)+"="+str(dictionary[key])+"&")
    return string[:-1]
    

class Account:
    """A class to represent a account
    
    insteance attributes
    * email: str
    * token: str
    * blance: int
    * request_log: list    
    """
    def __init__ (self, email, token, balance=-1, request_log=[]):
        """(str, int, int, list)->NoneType
        creat a object of type Account
        >>> my_acct = Account("rui-jia.meng@mail.mcgill.ca", "EKOXuP8G9QElneVp")
        >>> my_acct.email
        'rui-jia.meng@mail.mcgill.ca'
        >>> my_acct.token
        'EKOXuP8G9QElneVp'
        >>> my_acct.balance
        -1
        """
        if type(email) != str or type(token) !=str:
            raise AssertionError("email and token must be a string")
        elif str(email.split("@")[-1])!= "mcgill.ca" and str(email.split("@")[-1])!= "mail.mcgill.ca":
            raise AssertionError("the email must end in mcgill.ca")
        self.email = email
        self.token = token
        self.balance = -1
        self.request_log = request_log
    
    def __str__(self):
        """(NoneType)->NoneType
        return the email and the balance 
        >>>  my_acct = Account("ruijiameng@mcgill.ca", "idk")
        >>> print(my_acct)
        ruijiameng@mcgill.ca has balance -1
        >>>  my_acct = Account("rui-jia.meng@mail.mcgill.ca", "EKOXuP8G9QElneVp")
        >>> print(my_acct)
        rui-jia.meng@mail.mcgill.ca has balance -1
        >>>  my_acct = Account("rui-jia.meng@mail.mcgill.ca", "EKOXuP8G9QElneVp")
        >>> my_acct.retrieve_balance()
        1075
        >>> print(my_acct)
        rui-jia.meng@mail.mcgill.ca has balance 1075
        """
        return self.email+ " has balance " + str(self.balance)
    
    def call_api (self, endpoint, diction):
        """(str,dict)->dict
        return a dictionnary according to different endpoint
        >>>  my_acct = Account("rui-jia.meng@mail.mcgill.ca", "EKOXuP8G9QElneVp")
        >>> my_acct.call_api("balance", {'email': my_acct.email})
        {'message': 1075, 'status': 'OK'}
        
        >>>  my_acct = Account("rui-jia.meng@mail.mcgill.ca", "EKOXuP8G9QEln")
        >>> my_acct.call_api("balance", {'email': my_acct.email})
        Traceback (most recent call last):
        AssertionError: The token in the API request did not match the token that was sent over Slack.
        
        >>>  my_acct = Account("rui-jia.meng@mail.mcgill.ca", "EKOXuP8G9QElneVp")
        >>> my_acct.call_api("idk", {'email': my_acct.email})
        Traceback (most recent call last):
        AssertionError:  the endpoint need to be a balance or a transfer
        """
        
        api_string=""
        API_URL = 'https://coinsbot202.herokuapp.com/api/'
        if type(endpoint)!= str:
            raise AssertionError("the endpoint need to be a string")
        elif endpoint != "balance" and endpoint != "transfer":
            raise AssertionError(" the endpoint need to be a balance or a transfer")
        elif type(diction)!= dict:
            raise AssertionError(" the input must have a dictionnary")
        diction["token"]=str(self.token)
        api_string=endpoint+"?"+dict_to_query(diction)
        request_URL= API_URL+api_string
        result = requests.get(url=request_URL).json()
        if result["status"]!="OK":
            raise AssertionError(result["message"])
        return result
    
    def retrieve_balance(self):
        """(NoneType)->int
        return the instant attribute balance of the account obkect
        >>>  my_acct = Account("rui-jia.meng@mail.mcgill.ca", "EKOXuP8G9QElneVp")
        >>> my_acct.retrieve_balance()
        1075
        
        >>>  my_acct = Account("rui-jia.meng@mail.mcgill.ca", "EKOXuP8G9QEln")
        >>> my_acct.retrieve_balance()
        Traceback (most recent call last):
        AssertionError: The token in the API request did not match the token that was sent over Slack.
        
        >>>  my_acct = Account("rui-jia.meng@mail.mill.ca", "EKOXuP8G9QElneVp")
        Traceback (most recent call last):
        AssertionError: the email must end in mcgill.ca
        """
        self.balance= self.call_api("balance", {'email': self.email})["message"]
        return self.balance
        
        
    def transfer(self, integer, email):
        """(int, str)-> str
        return a string  of the transfer ammount, according to the input
        number of coins by calling api
        >>>  my_acct = Account("rui-jia.meng@mail.mcgill.ca", "EKOXuP8G9QElneVp")
        >>> my_acct.retrieve_balance()
        1075
        >>> my_acct.transfer(25, "jiaqi.yang4@mail.mcgill.ca")
        'You have transferred 25 coins of your balance of 1075 coins to jiaqi.yang4. Your balance is now 1050.'
        >>>  my_acct = Account("rui-jia.meng@mail.mcgill.ca", "EKOXuP8G9QElneVp")
        >>> my_acct.transfer(25, "jiaqi.yang4@mail.mcgill.ca")
        Traceback (most recent call last):
        AssertionError: ur balance is -1
        >>>  my_acct = Account("rui-jia.meng@mail.mcgill.ca", "EKOXuP8G9QElneVp")
        >>> my_acct.transfer(25, "rui-jia.meng@mail.mcgill.ca")
        Traceback (most recent call last):
        AssertionError: the email enter must be a different email than withdrawal email
        >>> 
        """
        if type(email)!= str:
            raise AssertionError("the email must a string")
        elif (email.split("@")[-1])!= "mcgill.ca" and (email.split("@")[-1])!= "mail.mcgill.ca":
            raise AssertionError("the email must end in mcgill.ca")
        elif type(integer) != int:
            raise AssertionError("the input must be a positive interger")
        elif integer < 0:
            raise AssertionError("the input must be a positive interger")
        elif email==self.email:
            raise AssertionError("the email enter must be a different email than withdrawal email")
        elif self.balance==-1:
            raise AssertionError("ur balance is -1")
        elif self.balance<0:
            raise AssertionError("ur balance is negative")
        elif self.balance < integer:
            raise AssertionError("the balance is not enough for transfer")
        return(self.call_api("transfer", {'withdrawal_email': self.email, "deposit_email": email, "amount": integer})["message"])
        
        
    