# Module imports
from re import S
import string
import mariadb
import sys
from user import *


# Establishes database connection
# Connect to MariaDB Platform - Try Clause
try:
    global conn
    conn = mariadb.connect(
        user = "root",
        password = "",
        host = "127.0.0.1",
        port = 3306,
        database = "cse_2213"
    )

# Connect to MariaDB Platform - Execption Handling
except mariadb.Error as e:
    print(f"\nError connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor - Used to execute queries
global cur
cur = conn.cursor()


# Defines an exit function
def EXIT():
    print("\nThank you for shopping! Have a nice day!")
    conn.close()
    sys.exit(0)


# Creates a boolean variable (and accompanying functions) to store the login state and toggle its value
# A Boolean value of 'True' means that the user has successfully logged in with valid credentials
# A Boolean value of 'False' means that the user has yet to successfully login; this bars entry into the more meticulous of the program; limits options

# Global variable
global login_status


# Accompanying Function
def login():
    return True
def logout():
    return False


# Creates a integer variable to store the menu choice

#Global variable
global choice


# Runs a SQL query to generate a list of users that currently exist in the database
def generate_User_List():
     # Uses cursor to run SQL query
    cur.execute(
        "Select * FROM Users;"
    )

    # Creates a list of users and populates it; used for searching for existing users
    user_list = []

    # Loops over the cursor to populate (append to) a list with the information gathered from a SQL query
    for (first_name, last_name, username, password, phone_number, street, city, state, zip, card_number, age) in cur:
        # Creates User Object using constructor
        user = User(first_name, last_name, username, password, phone_number, street, city, state, zip, card_number, age)
        # Appends User object to the user_list
        user_list.append(user)
    
    # Returns the current list of users
    return user_list


# Driver code
def main():
    # Initially sets global login status variable to 'False'; see above explanation for the definition of 'False'
    login_status = logout()


    # Welcome Message - prints off stylized greeting for the user

    print("*******************************************************************")
    print("*    Welcome! This is an e-commerce store that specializes        *")
    print("*    in the distribution of smartphones, pcs, gaming consoles,    *")
    print("*    and headphones.                                              *")
    print("*******************************************************************")

    # Prints off a newline character for formatting purposes
    print("")


    # Menuing - e-commerce store menu options

    # Establishes in infinite loop for to present the menu
    while(1):
        
        # Conditionally displays menu options based on login status
        if (login_status == False):
            print("[1] Login")
            print("[2] Create Account")
            print("[3] Exit Program")
        else:
            print("[1] Inventory Information")
            print("[2] Cart Information")
            print("[3] Order History")
            print("[4] User Profile")
            print("[5] Logout")
            print("[6] Exit Program")
        
        # Prints off a newline character for formatting purposes
        print("")


        # Tests for valid input (for the menu selection)
        try:
            choice = int(input("Select a menu option: "))

        # Catches a value error; specifically, the input to the prompt is of an invalid typing (or not an integer)
        except ValueError:
            print("\nAn error occurred! Enter in an integer.")

        # Catches a generic error; specifically, the clause will capture any error; granted, the error will remain unidentified
        except:
            print ("\nAn unknown error occurred! Try again!")


        # Proceeds with the program's execution
        else:
            # Choice [3] & [6] - Exit
            if ((choice == 3 and login_status == False) or (choice == 6 and login_status == True)):
                EXIT()


            # Choice [5] - Logout
            if (choice == 5 and login_status == True):
                login_status = logout()
            

            # Choice [1] - Login
            if (choice == 1 and login_status == False):
                # Creates a list of users and populates it; used for searching for existing users
                user_list = generate_User_List()
                
                # Prompts for the user's credentials (username and password)
                username = input("\nUsername: ")
                password = input("Password: ")

                # Loops over the elements in the user list acquired from running the SQL query (via the cursor)
                for i in range(len(user_list)):
                    # Prints out an indication of success if the customer's credentials matches an entry in the user list; redircts the user to the store's menu options; and toggles the global user status variable
                    if (username == user_list[i].username and password == user_list[i].password):
                        print("\nSuccessfuly logged in! *Redirecting user to store*")
                        login_status = login()
                        break
                
                # Prints out an indication of failure if the customer's credentials does not match an entry in the user list
                if (login_status == False):
                    print("\nInvalid credentials! Try again!")
            

            # Choice [2] - Create Account
            if (choice == 2 and login_status == False):
                # Checks whether the user input provided is of a valid type (strings, ints, floats, Booleans, etc.)
                try:
                    # Takes input from the user
                    first_name = str(input("\nEnter in your first name: "))
                    last_name = str(input("Enter in your last name: "))
                    username = str(input("Enter in a username: "))
                    password = str(input("Enter in a password: "))
                    phone_number = int(input("Enter in your phone number: "))
                    street = str(input("Enter in the street component of your address: "))
                    city = str(input("Enter in the city component of your address: "))
                    state = str(input("Enter in the state component of your address: "))
                    zip = int(input("Enter in the zip component of your address: "))
                    card_number = int(input("Enter in your credit card number: "))
                    age = int(input("Enter in your age: "))

                    # Creates a User object from the customer's input for comparison purposes
                    customer_user_obj = User(first_name, last_name, username, password, phone_number, street, city, state, zip, card_number, age)

                # Catches a value error
                except ValueError:
                    print("\nAn error occurred! Enter in an integer.")

                # Catches a generic error
                except:
                    print ("\nAn unknown error occurred! Try again!")

                # Proceeds with the program's execution
                else:
                    # Creates a list of users and populates it; used for searching for existing users  
                    user_list = generate_User_List()

                    # Loops over the elements in the user list acquired from running the SQL query (via the cursor)
                    for i in range(len(user_list)):
                        # Error 01: The user provides data that matches an existing user for every field; i.e., the user attempted to add a duplicate user to the database
                        if (customer_user_obj == user_list[i]):
                            print("\nThat information corresponds to an existing user! Select [1] to login with your credentials!")
                            break

                        # Error 02: The user provides valid (non-duplicate) data for every field save for the username; since every user must have a unique username (as it is the primary key in the database), this is considered an invalid user as well
                        elif (customer_user_obj < user_list[i]):
                            print("\nThat username has already been taken! Try again!")
                            break
                        # Acceptable User data
                        # Case 01: The user provides data that does not match an existing user for every field
                        # Case 02: The user provides data that does match an existing user for every field save for the username; the provided username must be unique given the database's constraints; models the unlikely but entirely possible scenario that the customer has 'n' siblings that all living within the same household, were born within the same year (note our design does not account for birthdays), use the same payment information, and share the same phone (perhaps it is a landline or house number)
                        elif (customer_user_obj > user_list[i] or customer_user_obj != user_list[i]):
                            # Builds query to insert into the database
                            query_string = """
                            INSERT INTO Users ( first_name, 
                                                last_name, 
                                                username, 
                                                password, 
                                                phone_number, 
                                                street, 
                                                city, 
                                                state, 
                                                zip, 
                                                card_number, 
                                                age) VALUES (   %s,
                                                                %s,
                                                                %s,
                                                                %s,
                                                                %s,
                                                                %s,
                                                                %s,
                                                                %s,
                                                                %s,
                                                                %s,
                                                                %s);"""

                            # Creates a tuple to store the customer's credentials so they can be passed into the query
                            # Leaves an additional slot open in the tuple
                            query_parameters = (customer_user_obj.first_name, 
                                                customer_user_obj.last_name,
                                                customer_user_obj.username,
                                                customer_user_obj.password,
                                                customer_user_obj.phone_number,
                                                customer_user_obj.street,
                                                customer_user_obj.city,
                                                customer_user_obj.state,
                                                customer_user_obj.zip,
                                                customer_user_obj.card_number,
                                                customer_user_obj.age, )

                            # Executes a canned-transaction to insert a new user into the database
                            cur.execute(query_string, query_parameters)

                            # Commits (finalizes) the changes to the database; without this statement, the database would not display the newly added user
                            conn.commit()

                            # Prints an indicator of success
                            print("\nA new account has been created! Select [1] to login with your credentials!")
                            break

            # Choice [4] - User Profile
            if (choice == 4 and login_status == True):
                while(1):
                    print("\n[1] Go back")
                    print("[2] Edit Shipping Information")
                    print("[3] Edit Payment Information")
                    print("[4] Delete Account")
                    

                    # Prints off a newline character for formatting purposes
                    print("")


                    # Tests for valid input (for the menu selection)
                    try:
                        choice = int(input("Select a menu option: "))

                    # Catches a value error; specifically, the input to the prompt is of an invalid typing (or not an integer)
                    except ValueError:
                        print("\nAn error occurred! Enter in an integer.")

                    # Catches a generic error; specifically, the clause will capture any error; granted, the error will remain unidentified
                    except:
                        print ("\nAn unknown error occurred! Try again!")


                    # Proceeds with the program's execution
                    else:
                        # Choice [1] - Go back
                        if (choice == 1):
                            break
                    
                    # Executes the additional break if the user chose choice [1]
                    if(choice == 1):
                        break



        # Prints off a newline character for formatting purposes
        print("")


    EXIT()


main()