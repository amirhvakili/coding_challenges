# Create an @authenticated decorator that only allows the function to run if user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': False
    # changing this will either run or not run the message_friends function.
}


def authenticated(fn):
    # code here
    def wrapper(*args, **kwargs):
        if (args[0]['valid']):
            return fn(*args, **kwargs)
        else:
            print('User is not authenticated')

    return wrapper


@authenticated
def message_friends(user):
    print('message has been sent')


message_friends(user1)
