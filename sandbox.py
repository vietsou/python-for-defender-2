mylist = ["picard", "riker", "troi", "worf", "LaForge", "Crusher"]

countlist = list(range(20))

elements = ["iridium", "osmium", "tantalum", "manganese" ]

mynewlist = [ i.capitalize() + " :)" for i in mylist]

##############

###-----MODULES-----###

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

