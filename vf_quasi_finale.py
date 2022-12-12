def norme_IEEE(n):
    if n == 0 :
        nombre = "0"*32
    else :
        nombre = "" + bit_de_signe(n) +"/"+ exposant_en_binaire(n) +"/" +mantisse_en_binaire(mantisse_en_decimal(n))
    return nombre

def bit_de_signe(n) :#definit le bit de signe du nombre en iee 754
    if n >= 0 :
        val_return = "0"
    else :
        val_return = "1"
    return val_return

def convertisseur_decimal_a_binaire(nbr):# transforme un nombre decimal en binaire pas dans le format ieee 754
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

def exposant_en_decimal(n):#exposant en décimal sans biais de l'esposant que j'utilise ppour la somme
    exposant=0
    n=abs(n)
    while n/(2**exposant)>=1:
        if n>=1:
            exposant+=1
        else:
            exposant-=1
    return exposant-1

def exposant_biaisé_en_décimal(n): 
    return exposant_en_decimal(n)-(2**(8-1))-1

def exposant_en_binaire(n):
   return convertisseur_decimal_a_binaire(exposant_biaisé_en_décimal(n))
 
def mantisse_en_decimal(n):#divise le nombre par 2puissance l'esxposant 
   return n/(2**exposant_en_decimal(n))

def mantisse_en_binaire(n):#transforme la mantisse de décimal a binaire
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
 
def somme_mantisse(a,b):#addition
    a = list(a.strip())
    b = list(b.strip())
    retenue = 0
    compteur = 0
    continuer = True
    mantisse_finale =[]
    while continuer == True:
        
        if compteur == 24 :
            # if retenue == 1:
            #     mantisse_finale.append(1)
            #     mantisse_finale.pop(0)
            break
        tatata = a[-(1+compteur)]
        bababa = b[-(1+compteur)]
        if a[-(1+compteur)] == "0" and b[-(1+compteur)] == "1" and retenue == 0 :
            retenue = 0
            mantisse_finale.append(1)
        elif  a[-(1+compteur)] == "1" and b[-(1+compteur)] == "0" and retenue == 0:
            retenue = 0
            mantisse_finale.append(1)
        elif a[-(1+compteur)] == "1" and b[-(1+compteur)] == "0" and retenue == 1 :
            retenue = 1
            mantisse_finale.append(0)
        elif a[-(1+compteur)] == "0" and b[-(1+compteur)] == "0" and retenue == 1:
            retenue = 0
            mantisse_finale.append(1)
        elif a[-(1+compteur)] == "0" and b[-(1+compteur)] == "1" and retenue == 1:
            retenue = 1
            mantisse_finale.append(0)
        elif a[-(1+compteur)] == "1" and b[-(1+compteur)] == "1" and retenue == 0:
            retenue = 1
            mantisse_finale.append(0)
        elif a[-(1+compteur)] == "1" and b[-(1+compteur)] == "1" and retenue == 1:
            retenue = 1
            mantisse_finale.append(1)
        else :
            retenue = 0
            mantisse_finale.append(0)
        compteur += 1
    mantisse_finale.reverse() 
    mantisse_finale_str = ''.join([str(i) for i in mantisse_finale ]) 
    return mantisse_finale_str

def exposant_sup(exp1,exp2):#determine l'exposant supérieur à l'autre (peut s'implement etre remplacer par "exposant_en_decimal(n1) ( > ou < ) exposant_en_decimal(n2)" mais bon)
    for i in range(0,len(exp1)):
        if int(exp1[i]) > int(exp2[i]):
            return (1)
        if int(exp1[i]) < int(exp2[i]):
            return (-1)

def ajouter_un(mantisse_a_ajouter):
  mantisse_a_ajouter_list = list(mantisse_a_ajouter)
  nbr = 0
  for i in range(len(mantisse_a_ajouter_list)):
    nbr += int(mantisse_a_ajouter_list[i]) * (2 ** (len(mantisse_a_ajouter_list) - i - 1))
  nbr += 1
  binary_number = ""
  while nbr > 0:
    binary_number = str(nbr % 2) + binary_number
    nbr //= 2
  return binary_number

def difference_exposant(exp_a,exp_b,wich_supp):
    compteur = 0
    if wich_supp == 0:
        return 0
    elif wich_supp == 1 :
        exposant_plus_petit = exp_a
        exposant_plus_grand = exp_b
    else:
        exposant_plus_petit = exp_b
        exposant_plus_grand = exp_a
    while exposant_plus_petit != exposant_plus_grand:
        exposant_plus_petit = ajouter_un(exposant_plus_petit)
        compteur += 1
    return compteur

def mantisse_a_additioner(compteur,mantisse):
    return "0"*compteur+mantisse[:-compteur]

def somme_IEEE(n1,n2):#utilise toute les fonctions d'avants pour faire la somme des 2 nombres
    #a une grosse

    final=[]

    final.append(bit_de_signe(n1))
    if exposant_sup(exposant_en_binaire(n1),exposant_en_binaire(n2))==1:
        final.append(exposant_en_binaire(n1))
        mantisse_1 = mantisse_a_additioner(difference_exposant(exposant_en_binaire(n1),exposant_en_binaire(n2),-1),mantisse_en_binaire(mantisse_en_decimal(n2)))
        mantisse_2 = mantisse_en_binaire(mantisse_en_decimal(n1)) 
    elif exposant_sup(exposant_en_binaire(n1),exposant_en_binaire(n2))==-1:
        final.append(exposant_en_binaire(n2)) 
        mantisse_1 = mantisse_a_additioner(difference_exposant(exposant_en_binaire(n1),exposant_en_binaire(n2),1),mantisse_en_binaire(mantisse_en_decimal(n1))) 
        mantisse_2 = mantisse_en_binaire(mantisse_en_decimal(n2))

    elif exposant_en_decimal(n1)==exposant_en_decimal(n2): 
        mantisse_1 = mantisse_en_binaire(mantisse_en_decimal(n1))
        mantisse_2 = mantisse_en_binaire(mantisse_en_decimal(n2))
        final.append(convertisseur_decimal_a_binaire(exposant_biaisé_en_décimal(n1)+1))

    
    final.append(somme_mantisse(mantisse_1,mantisse_2)) 
    #final.append(mantisse_1,mantisse_2)

 

    return final

    #final+=somme_mantisse(n1,n2)


#print(exposant_biaisé_en_décimal(2))
#print(somme_mantisse("0010","1100"))
#print(somme_mantisse("001000000000000000000000","110000000000000000000000"))
#print(mantisse_en_binaire(mantisse_en_decimal(2.5)))
print(somme_IEEE(854.85475,478.47512))
print("       ",norme_IEEE(854.85475))
# print(mantisse_en_decimal(12))
# print(exposant_en_decimal(12))
