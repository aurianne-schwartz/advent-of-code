# 1er décembre


#partie 1

#ouverture et lecture du fichier
f = open('input.txt', 'r')
lines = f.readlines()
f.close()

#res attendu
compteur = 0

nombre = ''
mini = ''


#liste = ['one','two','three','four','five','six','seven','eight','nine']

for line in lines:
    #print(line)
    for i in line:
        if i in ['0','1','2','3','4','5','6','7','8','9']:
            nombre += i

    if len(nombre) == 1:
        nombre += nombre


    #print(nombre)
    mini += nombre[0]
    mini += nombre[len(nombre)-1]

    #print(mini)
    compteur += int(mini)

    mini = ''
    nombre = ''

print("premier résultat")
print(compteur)

#partie 2

import re

#dico pour remplacer les chiffres str en num mais en laissant la première et la dernière lettre car peuvent constituer un autre chiffre
strennum = {
    "one": "o1e",
    "two": "t2o",
    "three": "t3e",
    "four": "f4r",
    "five": "f5e",
    "six": "s6x",
    "seven": "s7n",
    "eight": "e8t",
    "nine": "n9e",
}

#pour remplacer dans le texte les chiffres en lettres en int
def remplace(text):
    for k, v in strennum.items():
        text = text.replace(k, v)
    return text


#calcul de la somme des chiffres
def calibration(text):
    return sum(int(l[0] + l[-1]) for l in re.sub(r"[A-z]", "", text).split("\n"))


text = open("input.txt").read()
#print(calibration(text))
print("deuxième résultat")
print(calibration(remplace(text)))
