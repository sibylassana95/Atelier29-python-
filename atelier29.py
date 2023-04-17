# Ecrire un programme en langage Python qui demande à l’utilisateur 
# de saisir son âge et de lui afficher le message « vous êtes Majeur ! »
#  si l’âge tapé est supérieur ou égale à 18 et le message « vous êtes mineur ! »
#  si l’âge tapé est inférieur à 18

# Demander à l'utilisateur de taper son âge 
age = int(input("Tapez votre age : "))
if age > 18:
    print("Vous êtes majeur !")
else:
    print("Vous êtes mineur !")
    
    
 # En mode fonction
def demander_age():
    # Demander à l'utilisateur de taper son âge
    age = int(input("Tapez votre age : "))
    if age > 18:
        return print("Vous êtes majeur !")
    print("Vous êtes mineur !")

demander_age()
