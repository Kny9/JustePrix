#!/apt/homebrew/bin/python3

from random import randint

def jeu_juste_prix():
  print("bienvenue dans le juste prix !")

  juste_prix = randint(1, 100)  
  essai = 10 
  while essai >= 1:

    essai -= 1
          
    joueur_prix = int(input("Entrer un prix "))
  
    if joueur_prix == juste_prix:
      print("Trouvé ! Tu a découvert le juste prix !")
      break
    elif essai == 0:
      print(f"game over le prix était {juste_prix}")
      break
    elif joueur_prix > juste_prix:
      print("trop haut")

    elif joueur_prix < juste_prix:
      print("trop bas")

    print(f"il vous reste {essai} essaie")

jeu_juste_prix()

rejouer = input("Voulez-vous rejouer ? ")
    
if rejouer.lower() == "oui":
  jeu_juste_prix()

elif rejouer.lower() == "non":
  print("merci d'avoir joué !")

else:
  print("erreur : entré oui ou non !")


# fin du jeu après la boucle
print("Fin du jeu !")
