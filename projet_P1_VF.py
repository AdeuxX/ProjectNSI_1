def norme_IEEE(n):
    if n == 0 :
        nombre = "0"*32
    else :
        nombre = "" + bit_de_signe(n) +"/"+ exposant_en_binaire(n) +"/" +mantisse_en_binaire(mantisse_en_decimal(n))
    return nombre

def bit_de_signe(n) :
    if n >= 0 :
        val_return = "0"
    else : 
        val_return = "1"
    return val_return

def ConvertisseurDecimalToBase(nbr):
    liste = []
    base=2
    if nbr >= 0 :
        positif = True
    else:
        positif = False
        nbr = nbr * -1
    for i in range (0,8) :
        liste.append(nbr%base)
        nbr = nbr//base
    liste.reverse()
    if positif == False :
        for u in range (0,len(liste)):
            if liste[u] == 1:
                liste[u] = liste[u]-1
            else :
                liste[u] = liste[u] + 1
        if liste[7] == 0:
            liste[7] = 1
            #return (liste)
        else:
            continuer = True
            compteur = 0
            while continuer == True :
                if liste[7 - compteur] == 1 :
                    liste[7 - compteur] = 0
                else :
                    liste[7 - compteur] = 1
                    continuer = False
                compteur  = compteur +1
    string=""
    for i in liste:
        string = string + str(i)
    return string

def exposant_en_decimal(n):
    exposant=0
    n=abs(n)
    while n/(2**exposant)>=1:
        if n>=1:
            exposant+=1
        else:
            exposant-1
    return exposant-1


def exposant_biaisé_en_décimal(n):
    return exposant_en_decimal(n)-(2**(8-1))-1

def exposant_en_binaire(n):
   return ConvertisseurDecimalToBase(exposant_biaisé_en_décimal(n))

def mantisse_en_decimal(n):
   return n/(2**exposant_en_decimal(n))

def mantisse_en_binaire(n):
    mantisse = "1"
    n = n -1
    for i in range (1,24) :
        puissance_de_deux = 2**-i
        if n - puissance_de_deux < 0 :
            mantisse = mantisse + "0"
        elif n - puissance_de_deux > 0 :
            mantisse = mantisse + "1"
            n = n - puissance_de_deux
        elif n - puissance_de_deux == 0 :
            mantisse = mantisse + "1"
            return mantisse.ljust(23,"0")
    return mantisse

def somme_mantisse(a,b):
    retenue = False
    compteur = 0
    continuer = True
    mantisse_finale =[]
    while continuer == True:
        if a[-(1-compteur)] == 0 and b[-(1-compteur)] == 1:
            retenue = False
            mantisse_finale.append(1)
        elif  a[-(1-compteur)] == 1 and b[-(1-compteur)] == 0:
            retenue = False
            mantisse_finale.append(1)
        elif a[-(1-compteur)] == 1 and b[-(1-compteur)] == 0:
            retenue = True
            mantisse_finale.append(0)
        elif a[-(1-compteur)] == 0 and b[-(1-compteur)] == 0 and retenue == True:
            retenue = False
            mantisse_finale.append(1)
        elif a[-(1-compteur)] == 1 and b[-(1-compteur)] == 0 and retenue == True:
            retenue = True
            mantisse_finale.append(0)
        elif a[-(1-compteur)] == 0 and b[-(1-compteur)] == 1 and retenue == True:
            retenue = True
            mantisse_finale.append(0)
        else :
            retenue = False
            mantisse_finale.append(0)
        compteur += 1
#REGARDER BIAIS DE L4ESPOSANT SUR WIKIPEDIA POUR REPONDRE



print(norme_IEEE(13.5))
