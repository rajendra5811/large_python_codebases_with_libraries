email=input("enter a email")
def validate_email(email):
    """ Test if an email is of a valid format """
   
    if type(email) is not str:
        raise Exception('Email is not a String')

    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    if not re.search(regex,email):
        raise Exception('Email is Malformed')
    
    return True
validate_email(email)