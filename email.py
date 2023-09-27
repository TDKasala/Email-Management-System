# Creating a class called Email and adding the variables

class Email:
    def __init__(self, email_contents, from_address):
        self.from_address = from_address
        self.is_spam = False
        self.has_been_read = False
        self.email_contents = email_contents

   # Creating a function called mark_as_read

    def mark_as_read(self):
        self.has_been_read = True

   # Creating a function called mark_as_spam
   
    def mark_as_spam(self):
        self.is_spam = True
        
# Creating an empty list called 'inbox' to store all emails

inbox = []

# Creating a method called 'add_email' to add all emails.

def add_email(email_contents, from_address):
    email = Email(email_contents, from_address)
    inbox.append(email)


# Creating a method called 'get_count' to count all emails.

def get_count():
    return len(inbox)


# Creating a method to get emails and return the contents

def get_email(index):
    if 0 <= index < len(inbox):
        inbox[index].mark_as_read()

        return inbox[index].email_contents, inbox[index].from_address
    else:
        print('Invalid index, email does not exist')


# Creating a method that gets all unread emails.

def get_unread_emails():
    unread_list = []
    for i in inbox:
        if not i.has_been_read:
            unread_list.append(i)
    return unread_list


# creating a method that gets all emails marked as spam.

def get_spam_emails():
    spam_list = []
    for i in inbox:
        if i.is_spam:
            spam_list.append(i)
            print(f"spam: {i.email_contents}")
    return spam_list


# Creating a method that add all spams.

def add_spam(index):
    messages = inbox[index]
    messages.mark_as_spam()
    print("Email added to spam")


# creating a function that delete emails.

def delete():
    if len(inbox) > 0:
        return inbox.pop()
    else:
        print('Error, could not delete email')


# Emails with message

init_emails = [
    'Hello Denis, deniskasala17@gmail.com',
    'Hello Landry, landrykasala@yahoo.com'
]

for i in init_emails:
    message, email = i.split(',')
    add_email(message, email)

user_choice = ""

while user_choice != "quit":
    user_choice = input(
        "What would you like to do - read/mark spam/send/quit?: ")
    
    if user_choice == "read": 
        print("List of unread email\n")
        print(type(inbox))
        for i, mail in enumerate(init_emails):
            print(f'{i + 1}. {mail}')
        num = int(input("\nPlease ennter the number of email you want to read: "))
        print(get_email(num - 1))

    elif user_choice == "mark spam": 
        print("List of emails\n: ")
        for i, mail in enumerate(init_emails):
            print(f'{i}. {mail}')
        num = int(input("\nEnter number of email you want to spam: "))
        add_spam(num - 1)
        get_spam_emails()

    elif user_choice == "send": 
        from_address = input("Enter your email address: ")
        email_contents = input("Enter email content: ")
        add_email(email_contents, from_address)
        print("Email sent successfully!")

    elif user_choice == "quit":
        print("Goodbye")
        
    else:
        print("Oops - incorrect input")
