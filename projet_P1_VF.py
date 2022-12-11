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

            exposant=exposant-1

    return exposant

 

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

    retenue = 0

    compteur = 0

    continuer = True

    mantisse_finale =[]

    while continuer == True:

        if compteur == len(a):

            continuer = False

        if a[-(1-compteur)] == 0 and b[-(1-compteur)] == 1 and retenue == 0 :

            retenue = 0

            mantisse_finale.append(1)
        elif  a[-(1-compteur)] == 1 and b[-(1-compteur)] == 0 and retenue == 0:
            retenue = 0
            mantisse_finale.append(1)
        elif a[-(1-compteur)] == 1 and b[-(1-compteur)] == 0 and retenue == 1 :
            retenue = 1
            mantisse_finale.append(0)
        elif a[-(1-compteur)] == 0 and b[-(1-compteur)] == 0 and retenue == 1:
            retenue = 0
            mantisse_finale.append(1)
        elif a[-(1-compteur)] == 0 and b[-(1-compteur)] == 1 and retenue == 1:
            retenue = 1
            mantisse_finale.append(0)
        elif a[-(1-compteur)] == 1 and b[-(1-compteur)] == 1 and retenue == 0:
            retenue = 1
            mantisse_finale.append(0)
        elif a[-(1-compteur)] == 1 and b[-(1-compteur)] == 1 and retenue == 1:
            retenue = 1
            mantisse_finale.append(1)
        else :
            retenue = False
            mantisse_finale.append(0)
        compteur -= 1

    return mantisse_en_binaire.reverse()

 

def exposant_sup(exp1,exp2):

    for i in range(0,len(exp1)):

        if int(exp1[i]) > int(exp2[i]):

            return (1)

        if int(exp1[i]) < int(exp2[i]):

            return (-1)

        if int(exp1[i]) == int(exp2[i]):

            return(0)

def difference_exposant(exp_a,exp_b,wich_supp):
    if wich_supp == 0:
        return 0
    elif wich_supp == 1 :
        exposant_plus_petit = exp_a
        exposant_plus_grand = exp_b
    else:
        exposant_plus_petit = exp_b
        exposant_plus_grand = exp_a
    return int(exposant_plus_grand,2) - int(exposant_plus_petit,2)
###############################
#On a pas réussi a faire fonctionner le programme pour calculer la différence entre les 2 exposants sans convertir en décimale
#Mais voici le programme quasi fonctionnel que l'on avait fait: 
def difference_exposant_non_fontionnel(exp_a,exp_b,wich_supp):
    compteur = 0
    compteur_liste1 = 0
    compteur_final = 0
    if wich_supp == 0:
        return 0
    elif wich_supp == 1 :
        exposant_a_modif = exp_a
        condition = exp_b
    else:
        exposant_a_modif = exp_b
        condition = exp_a
    while exposant_a_modif != condition :
        liste_1 = [1 for i in range(0,1+compteur_liste1)]
        a = list(reversed(list(reversed(exposant_a_modif))[0:1+compteur_liste1]))
        if a == liste_1:
            exposant_a_modif[-(2+compteur_liste1)] = 1
            for i in range (0,compteur_liste1+1):
                compteur_final +=1
                exposant_a_modif[-(1+i)] = 0
            compteur = 0
            compteur_liste1 = 0
        elif exposant_a_modif[-(1+compteur)]== 1 :
            exposant_a_modif[-(1+compteur)]=0
            exposant_a_modif[-(2+compteur)]=1 
            compteur+= 1
            compteur_liste1 = 0 
#le probleme est a cette ligne là. le compteur_liste1 est augmenter une fois de trop dans certaine condition mais on arrive pas a règler ca
        elif exposant_a_modif[-(1+compteur)]== 0 and (exposant_a_modif[-compteur] == 0 or exposant_a_modif[-compteur] == None) :
            exposant_a_modif[-(1+compteur)] = 1
            compteur += 1
            compteur_liste1 += 2
        elif exposant_a_modif[-(1+compteur)]== 0 and exposant_a_modif[-compteur]== 1:
            exposant_a_modif[-(1+compteur)] = 1
            exposant_a_modif[-compteur] = 0
            compteur = 0
            compteur_final+= 1
        compteur_final +=1
    return compteur_final-1
#######################   

def mantisse_a_additioner(compteur,mantisse):
    return "0"*compteur+mantisse

 

def somme_IEEE(n1,n2):

    final=[]

    final.append(bit_de_signe(n1))

    if exposant_sup(exposant_en_binaire(n1),exposant_en_binaire(n2))==1:

        final.append(exposant_en_binaire(n1))

    if exposant_sup(exposant_en_binaire(n1),exposant_en_binaire(n2))==-1:

        final.append(exposant_en_binaire(n2))

    if exposant_sup(exposant_en_binaire(n1),exposant_en_binaire(n2))==0:

        final.append(exposant_en_binaire(n1))
    final.append(somme_mantisse(mantisse_en_binaire(mantisse_en_decimal(n1)),mantisse_en_binaire(mantisse_en_decimal(n2))))


 

    return(final)

    #final+=somme_mantisse(n1,n2)




 

#print(norme_IEEE(13.5))

 

#print(exposant_biaisé_en_décimal(2))

 

print(somme_IEEE(2,12))
