# Program AGENDA
def create_entry():
    """Creates an entry to the agenda."""
    cad_contato = {'name': str,
                   'address': str,
                   'telephone': int,
                   }
    cad_contato['name'] = input('Enter a name: ')
    cad_contato['address'] = input('Enter an address: ')
    cad_contato['telephone'] = input('Enter a telephone: ')
    return cad_contato

def verify_option():
    """Verifies an entry option."""
    verified_var = None
    user_option = input("Do you want to add more contacts? [Y]es, [N]o: ")
    while user_option.lower() != 'y' and user_option.lower() != 'n':
        print(f"Invalid option, please try again!")
        user_option = input("Do you want to add more contacts? [Y]es, [N]o: ")

    if user_option.lower() == 'y':
        verified_var = True
    elif user_option.lower() == 'n':
        verified_var = False
    return verified_var

def create_agenda():
    """Creates an agenda."""
    agenda = []
    active = True
    while active:
        print("Enter the contact's information!.")
        elem_contact = create_entry()
        agenda.append(elem_contact)
        print(f"Nice, you have entered {elem_contact['name'].title()}!")
        active = verify_option()
    return agenda

def show_agenda(agenda: dict):
    """Shows an agenda's information."""
    print("The Agenda's summary is:")
    for contact in agenda:
        for k, v in contact.items():
            print(f"\t{k.title()}: {v.title()}.")
        print("---")

minha_agenda = create_agenda()
show_agenda(minha_agenda)

