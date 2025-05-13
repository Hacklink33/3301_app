import random
import string
import pandas as pd
import gender_guesser.detector as gender
from faker import Faker
import random_address

class Email:
    def __init__(self) -> None:
        self.characterList = string.ascii_letters + string.digits
        self.email = []

    def generate(self) -> string:
        for i in range(30):
            randomchar = random.choice(self.characterList)
            self.email.append(randomchar)
        self.email = "".join(self.email)
        self.email += "@gmail.com"
        return self.email

class Password:
    def __init__(self) -> None:
        self.characterList = string.ascii_letters + string.digits + string.punctuation
        self.password = []
    def generate(self) -> string:
        for i in range(30):
            randomchar = random.choice(self.characterList)
            self.password.append(randomchar)
        self.password = "".join(self.password)
        return self.password

class Birthday:
    def __init__(self) -> None:
        self.day = str(random.randint(1, 31))
        self.month = str(random.randint(1, 13))
        self.year = str(random.randint(1950, 2005))
        self.birthday =  ''

    def generate(self) -> string:
        self.birthday = self.day + ' ' + self.month + ' ' + self.year #24 11 2003
        return self.birthday

class Username:
    def __init__(self) -> None:
        self.letters = string.ascii_letters
        self.numbers = string.digits
        self.username = ''

    def generate(self) -> string:
        first_half = ''.join([random.choice(self.letters) for i in range(7)])
        second_half = ''.join([random.choice(self.numbers) for i in range(4)])
        self.username = first_half + second_half
        return self.username
    
class Name:
    def __init__(self):
        self.fake = Faker()
        self.name = ((self.fake).name())
    def generate(self) -> string:
        fullname = f'{self.name}'
        first_name, last_name = fullname.split()
        return [first_name, last_name]
    def generate_firstname(self):
        fullname = f'{self.name}'
        first_name, x = fullname.split()
        return first_name
    def generate_lastname(self):
        fullname = f'{self.name}'
        x, last_name = fullname.split()
        return last_name
    
class Gender:
    def __init__(self) -> None:
        self.gd = gender.Detector()
        self.gender = ''
    def generate(self, name) -> string:
        self.gender = self.gd.get_gender(name)
        if 'female' in self.gender:
            self.gender = 'female'
            return self.gender
        elif 'male' in self.gender:
            self.gender = 'male'
            return self.gender
        else:
            self.gender = 'unknown'
            return self.gender

class Adress:
    def __init__(self) -> None:
       self.address_data = pd.read_csv('addresses.csv')
       self.random_address = self.address_data.sample()

    def generate(self) -> string:
        return self.random_address[['street', 'city', 'state', 'postal_code']].to_string(index=False)

class Phone:
    def __init__(self) -> None:
        return
    
class Photo:
    def __init__(self) -> None:
        return
        
Email1 = Email()
print(Email1.generate())

Pass1 = Password()
print(Pass1.generate())

Birth1 = Birthday()
print(Birth1.generate())

User1 = Username()
print(User1.generate())

Name1 = Name()
print(Name1.generate_firstname())
print(Name1.generate_lastname())

Gender1 = Gender()
print(Gender1.generate(Name1.generate_firstname()))

Adress1 = Adress()
print(Adress1.generate())