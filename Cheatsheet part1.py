# https://mybinder.org/v2/gh/vietsou/python-for-defenders/a316ff8ce6cc8beffea9b599592298997f48e30a?urlpath=lab%2Ftree%2F001.ipynb

# output
print("Hello World")

# input
name = input("What is your name ? ")

###-----NUMBERS------###

# irrational 
irrational = 10/3
print(irrational)

# rounded
arrondi = round(10/3, 2)
print(arrondi)



###-----LIST & TUPLES-----###

## LISTS
mylist = ["Picard", "Riker", "Troi", "Worf", "LaForge", "Crusher"]
mylist[2]
mylist[2:5]
mylist[2:6:2]
mylist[::-1]

# append()
mylist.append("Ro")

# pop()
mylist.pop() # remove last item
mylist.pop("Troi") # remove first encountered item

popedcrew = [] 
popedcrew.append(mylist.pop(2))  # put removed item into a list
print(popedcrew) 

# insert()
mylist.insert(4,"Carol")

# remove()
mylist.remove("Carol") # attention to error if doesn't exist

# enumerate()
print(enumerate(mylist)) 
    # <enumerate object at 0x71fc6f6fc810>

for index, staff in enumerate(mylist):
    print(index, staff)

    # 0 Picard
    # 1 Riker
    # 2 Troi
    # 3 Worf
    # 4 LaForge
    # 5 Crusher


## TUPLES
mytuple = (3,5,8,12,96)

# convert into list
mytupletolist = list(mytuple)

# list comprehension
mynewlist = [ i.capitalize() + " :)" for i in mylist]
nombres_x2 = [ i*2 for i in range(10)]
# nom_de_list = [ action sur l'itérateur for iterateur in nom_de_liste_ou_range]

###-----LOOPS-----###

# for loop
liste_exclaimed = []
for i in mylist:
    liste_exclaimed.append(i.capitalize() + "!")

# while loop
c = 10
while not c == 0:
    print(c)
    c -= 1
print("BANG!")

# useless while loop
found = False
count = 0

while not found:
    el = mylist[count]
    print(el)
    count+=1
    if el == "Worf":
        found = True
        print("Found it!")

# use this instead
if "Worf" in mylist:
    print ("Found it!")




###----FUNCTIONS------###

def greet(name = "You"):
    print(f"Hello {name}, hope you are good !")

for j in [ greet(i) for i in mylist ]:
    print(j)

# chaining functions

print("Python".replace("o","O").replace("t","7")) # etc

def l33t(nom):
    return nom \
        .replace("e", "3") \
        .replace("s", "5") \
        .replace("t", "7") 
        # etc

greet(l33t("Taggart")) 
    # Hello T4gg4r7, hope you are good!")"




###----CLASSES------###

# Définition de la classe
class Car:  

    # constructor : "__init__"
    def __init__(self, year, make, model, top_speed): # uniquement pour la création d'instances, pas pour les fonctions
        self.year = year
        self.make = make
        self.model = model
        self.top_speed = top_speed
        self.current_speed : int = 0

# __str__ va indiquer à la class comment retourner le print() d'une instance de classe
    def __str__(self):
        return f"I am a {self.year} {self.make} {self.model} that can go up to {self.top_speed} mph."
    
# fonction accelerate
    def accelerate(self):
        """
        Augmente la vitesse (current_speed)
        """
        self.current_speed += 10
        if self.current_speed >= self.top_speed:
            self.current_speed = self.top_speed

# fonction accelerate
    def brake(self):
        """
        Diminue la vitesse (current_speed)
        """
        self.current_speed -= 10
        if self.current_speed <= 0:
            self.current_speed = 0

# création d'une instance
kitt = Car(1982, "Pontiac", "Firebird Trasn Am", 124)

print(kitt)
    # avec __str__ : <__main__.Car object at 0x7ac1ac08b350>
    # sans __str__ : I am a 1982 Pontiac Firebird Trasn Am that can go up to 124 mph.  


## Child & Parent class

# définition de la classe parent
class mainIndicator:
    def __init__(self, value):
        self.value: str = value

    def defang(self) -> str:
        pass

# 1ere classe enfant
class IPv4Indicator(mainIndicator):
    def __init__(self, value):
        super().__init__(value)

    def defang(self) -> str:
        return self.value.replace(".","[.]")

# 2eme classe enfant    
class domainIndicator(mainIndicator):
    def __init__(self, value):
        super().__init__(value)

    def defang(self) -> str:
        return self.value.replace(".","[.]")
    

bad_ip = IPv4Indicator("192.168.1.1")
bad_domain = domainIndicator("evil.corp")

print(bad_ip.defang())
    # 192[.]168[.]1[.]1
print(bad_domain.defang())
    # evil[.]corp




###-----MODULES-----###
from random import choice

hasard = choice(10)
print(hasard)

# module requests
# https://www.w3schools.com/python/module_requests.asp

import requests
from pprint import pprint 

def get_website(url: str):

    try:
        r = requests.get(url)
        # Gestion des codes HTTP d'erreur (400 et plus)
        if r.status_code >= 400:
            print(f"Erreur HTTP {r.status_code}: {r.reason}")
            return None
        return r
    
    except requests.exceptions.RequestException as e:
        # Gestion des erreurs de connexion, timeout, etc.
        print("Echec de la requête :", e)
        return None



site = get_website("https://www.w3schools.com/python/module_requests.asp")
if site:
    pprint(site.text)
    pprint(site.headers)
    pprint(site.status_code)
    pprint(site.ok)
    pprint(site.elapsed)
# all methods on https://www.w3schools.com/python/ref_requests_response.asp



###-----__init__.py-----###

# Le fichier __init__.py peut être vide, mais il est souvent utilisé pour :
#     - Marquer la racine d'un package
#     - Initialiser des variables ou configurations,
#     - Importer des sous-modules pour simplifier l'accès,
#     - Définir des métadonnées du package,
#     - Spécifier l’API publique du package avec __all__.

# exemple

# Docstring pour le package
"""
my_package - Un package d'exemple

Contient :
- Class1 et function1 de module1
- Class2 de module2
"""

# Imports pour simplifier l'usage du package
from .module1 import Class1, function1
from .module2 import Class2

# Métadonnées
__version__ = "1.0.0"
__author__ = "Votre Nom"

# Définir ce qui est exposé avec `from my_package import *`
__all__ = ['Class1', 'function1', 'Class2']