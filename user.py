class User:
    # Null Constructor
    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.username = ""
        self.password = ""
        self.phone_number = 0
        self.street = ""
        self.city = ""
        self.state = ""
        self.zip = 0
        self.card_number = 0
        self.age = 0
    
    # Constructor
    def __init__(self, first_name, last_name, username, password, phone_number, street, city, state, zip, card_number, age):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.phone_number = phone_number
        self.street = street
        self.city = city
        self.state = state
        self.zip = zip
        self.card_number = card_number
        self.age = age

    # Setters
    def set_Street(self, street):
        self.street = street
    def set_City(self, city):
        self.city = city
    def set_State(self, state):
        self.state = state
    def set_Zip(self, zip):
        self.zip = zip
    def set_Card_Number(self, card_number):
        self.card_number = card_number

    # Getters
    def get_First_Name(self):
        return self.first_name
    def get_Last_Name(self):
        return self.last_name
    def get_Username(self):
        return self.username
    def get_Password(self):
        return self.password
    def get_Phone_Number(self):
        return self.phone_number
    def get_street(self):
        return self.street
    def get_City(self):
        return self.city
    def get_State(self):
        return self.state
    def get_Zip(self):
        return self.zip
    def get_Card_Number(self):
        return self.card_number
    def get_Age(self):
        return self.age

    # Operator Overloads - Equivalence
    # Note that the integer attributes are casted to an integer type; the source code stores the user's credentials in a string list; the casting is needed to compare a User object (of custom type User) to that of a list of User objects (which is recognized as the custom type User but converts all fields to the overarching list type string)
    def __eq__(self, other):
        if (isinstance(other, self.__class__)):
            return (self.first_name == other.first_name and
                    self.last_name == other.last_name and
                    self.username == other.username and
                    self.password == other.password and
                    self.phone_number == int(other.phone_number) and
                    self.street == other.street and
                    self.city == other.city and
                    self.state == other.state and
                    self.zip == int(other.zip) and
                    self.card_number == int(other.card_number) and
                    self.age == int(other.age))
        else:
            return (False)

    def __ne__(self, other):
        if (isinstance(other, self.__class__)):
            return (self.first_name != other.first_name and
                    self.last_name != other.last_name and
                    self.username != other.username and
                    self.password != other.password and
                    self.phone_number != int(other.phone_number) and
                    self.street != other.street and
                    self.city != other.city and 
                    self.state != other.state and
                    self.zip != int(other.zip) and
                    self.card_number != int(other.card_number) and
                    self.age != int(other.age))
        else:
            return (False)

# Customizes the less than (<) operator to check whether the customer's input is valid (not comprised of duplicate data) save for the provided username
    def __lt__(self, other):
        if (isinstance(other, self.__class__)):
            return (self.first_name != other.first_name and
                    self.last_name != other.last_name and
                    self.username == other.username and
                    self.password != other.password and
                    self.phone_number != int(other.phone_number) and
                    self.street != other.street and
                    self.city != other.city and 
                    self.state != other.state and
                    self.zip != int(other.zip) and
                    self.card_number != int(other.card_number) and
                    self.age != int(other.age))
        else:
            return (False)

    # Customizes the greater than (>) operator to check whether the customer's input is invalid (comprised of duplicate data) save for the provided username    
    def __gt__(self, other):
        if (isinstance(other, self.__class__)):
            return (self.first_name == other.first_name and
                    self.last_name == other.last_name and
                    self.username != other.username and
                    self.password == other.password and
                    self.phone_number == int(other.phone_number) and
                    self.street == other.street and
                    self.city == other.city and 
                    self.state == other.state and
                    self.zip == int(other.zip) and
                    self.card_number == int(other.card_number) and
                    self.age == int(other.age))
        else:
            return (False)
        
        