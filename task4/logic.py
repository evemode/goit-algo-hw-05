from functools import wraps

def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "No such name"
        except IndexError:
            return "Not enough info"

    return inner

@input_error
def parse_input(user_input):
    '''parsing user's input'''
    cmd, *args = user_input.split() #separates command from users additional info -  name, number
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    '''adds contact to contacts. Check main.py'''
    name, phone = args
    contacts[str(name)] = int(phone)  #adding itself
    return "Contact added."

@input_error
def change_contact(args, contacts):
    '''changes contact according to the info provided by user'''
    name, phone = args
    contacts.update({name:phone})
    result = 'Contact added'
    if name in contacts.keys(): #checks if contact exists
        contacts.update({name:phone})
    else:
        result ='No contact found'
    return result

@input_error
def show_phone(args, contacts):
    '''show contact :P'''
    name = args[0]
    return contacts[name]
    #result = 'No such contact'
    #if name in contacts.keys(): #checks if contact exists
        #result = contacts[name]
    #return result

def show_all(contacts):
    '''shows all contacts user has'''
    return "\n".join(f"{name} {number}" for name, number in contacts.items())
