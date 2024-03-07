
from dataclasses import dataclass
from enum import Enum


class Allergen(Enum):
    WHEAT = 'wheat'
    SUCROSE = 'sukrose'
    LACTOSE = 'lactose'


@dataclass
class Ingredient:
    name: str
    allergens: list[Allergen] = list


@dataclass
class MenuItem:
    name: str
    






#example function
#def funksjon():
    #pass

#Funksjon navn: snake_case
#class navn: PascalCase
#varibel navn: snake_case
#Konstnant navn: UPPER_CASE

class Epost:
    def __init__(self, epost: str):
        if '@' not in epost:
            raise ValueError('Ugyldig e-post, sjekk e-posten om den har riktig stavelse')

        self.navn = epost.split('@')[0]
        self.domene = epost.split('@')[1]

    def __str__(self):
        return f'{self.navn}@{self.domene}'

#epost = Epost('mitt-navn@domene.yep')
#print(epost.navn + '@' + epost.domene)


@dataclass
class Customer:
    first_name: str
    last_name: str
    email: Epost

    def __str__(self):
        return f'{self.first_name} {self.last_name} <{self.email}>'

    @property
    def name(self):
        return f'{self.first_name} {self.last_name}'


    #Unødvendig funksjon, fun tho
    #def say(self, message: str):
        #print( f'{self.name} says "{message}".')

    #def punch(self,target):
        #print(f'{self.name} punches {target.name} - {target.name} took 50 damage')


#customer = Customer('Jens', 'Stoltenberg', Epost'Jens@stoltenberg.no')
customer = Customer(first_name='Jens',last_name='Stoltenberg',email=Epost('Jens@stoltenberg.no'))

customer_2 = Customer(first_name='Erna',last_name='Solberg',email=Epost('Erna86@hotmail.com'))

print(customer)
#print(customer.email)
print(customer_2)
#print(customer.name)
#customer.say('If you use inbibitor and dan hung on the same team you can unlock Luigi.')





#Memories break line - Memories break line - Memories break line - Memories break line - Memories break line - Memories break line - Memories break line - Memories break line - Memories break line - Memories break line -

#as long as this is true will keep trying to use a take inn an input that fits our current criteria
#while True:
    #try:
        #epost = Epost(input('Skriv in din e-post addresse:'))
        #break
    #except ValueError:
        #print('Ugyldig e-post, prøv igjen')
#print(epost)

#epost = Epost('mitt-navn@domene.yep')
#print(epost)
#print(epost.navn + '@' + epost.domene)