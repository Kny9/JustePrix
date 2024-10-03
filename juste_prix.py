#!/apt/homebrew/bin/python3

from random import randint

def jeu_juste_prix():
    print("bienvenue")

    juste_prix = randint(1, 100)  
juste_prix = 9
essai = 10

running = True
joueur_prix = True
  
while essai<=10:
         
    joueur_prix = int(input("Entrer un prix "))
 
    if joueur_prix == juste_prix:
     print("Trouvé !")
     running = False
     
     

    elif joueur_prix > juste_prix:
     print("trop haut")
     essai -= 1
     print(f"il vous reste {essai} essaie")
       

    elif joueur_prix < juste_prix:
     print("trop bas")
     essai -= 1
     print(f"il vous reste {essai} essaie")

    rejouer = input("Voulez-vous rejouer ? ")
    if rejouer.lower() == "oui":
      jeu_juste_prix()

    elif rejouer.lower() == "non":
      break
    else:
      print("merci d'avoir joué !")

    





# fin du jeu après la boucle
print("Fin du jeu !")
 

