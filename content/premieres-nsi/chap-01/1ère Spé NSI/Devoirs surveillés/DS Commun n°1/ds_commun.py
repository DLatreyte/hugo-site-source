1)	Je veux faire la somme des éléments contenus dans une liste L . Le résultat étant mis dans une variable somme. Quelle est la bonne syntaxe :
a)	Somme=0
For i in range (L):
	Somme=Somme+i
b)	Somme=0
For I in range (len(L)) :
	Somme=Somme+i
c)	Somme=0
For I in L:
	Somme = i
d)	Somme=0
For I in range (len(L)):
	Somme=somme+L[i]

2)	Combien vaut la variable n à la fin de l’exécution:
n=2
For i in range (1,3) :
	n=n*2
a)	8		b) 4		c) 2		d) 16

3)	Combien vaut la variable n à la fin de l’exécution.
n=5
for i in range (4) :
	if i%2==0:
		n=n+3*i//2
	else:
		n=n-1
a)	6		b) 12		c) 1		d)10

4)	Que  renvoi cette ligne de commande :  3+2==6 and 1/0
a)	True		b) False		c) Une erreur		d)  11



5)	Combien vaut n à la fin de l’exécution ?
n=3
for i in range (4) :
	if n%2==0:
		n=n+i
	else :
		n=n+2i
a)	9		b) 14		c) 15		d) 20

6)	Si on a la liste L=[1,2,3,4] la commande   L.append(0)   sert à :
a)	Modifier la liste comme suit : L=[0,1,2,3,4]
b)	Renvoyer la valeur 1
c)	Modifier la liste comme suit : L=[1,2,3,4,0]
d)	Modifier la liste comme suit : L=[2,3,4]

7)	La conversion en base 2 du nombre 10 est :
a)	0101	b) 1001		c) 1100		d) 1010

8)	Si le dernier chiffre dans l’écriture en base 2 d’un nombre se termine par 0, que peut-on dire de ce nombre ?
a)	Il est premier	b) Il est paire	c) il est divisible par 10	d) il est plus grand que 9

9)	Que vaut n à la fin de l’exécution.
n=10
while n>11 :
	n=n-2
a)	8		b) 9		c) 10		d) l’algorithme ne s’arrête pas

10)	Que vaut n à la fin de l’exécution.
n=10
while n<11 :
	n=n-2
a)	8		b) 9		c) 10		d) l’algorithme ne s’arrête pas

11)	Soit la liste L=[‘jeudi’,’vendredi’,’samedi’] Que renvoi len(L)
a)	3		b) Une erreur		c) 5	d)19 



12)	La fonction suivante prend une liste en paramètre. A quoi sert-elle ?
Def f_mystere (L) :
	var=L[0]
For i in range (1,len(L)) :
	If L[i]>var:
		Var=L[i]
Return var

a)	La fonction renvoi la somme de tous les éléments.
b)	La fonction renvoi la moyenne de tous les éléments
c)	La fonction renvoi la plus grande valeur de tous les éléments
d)	La fonction renvoi la plus petite valeur de tous les éléments


13)	Que renvoi cette commande :    3==2+2  or  1/0
a)	True		b) False		c) Une erreur		d)  11

14)	Que renvoi cette commande :    3==3*1  or  1/0
b)	True		b) False		c) Une erreur		d)  11
15)	Que fait ce petit programme :
Nbsaisie=int(input(‘combien de nombre voulez vous saisir ?’)
Var_mysterieuse=0
For i in range (Nbsaisie) :
	Nombre=int(input(‘saisissez un nombre’))
	Var_mysterieuse= Nombre + Var_mysterieuse
Print (‘ le resultat est’,Var_mysterieuse/ Nbsaisie)

a)	Il permet de saisir un certain nombre de valeurs voulue et d’en donner la moyenne.
b)	Il permet de saisir un certain nombre de valeurs et voulue et d’en donner la somme.
c)	Il permet de saisir un certain nombre de valeurs et voulue et de les afficher.
d)	Le programme comporte une erreur.

16)	Combien de fois le mot ‘ok’ sera-t-il affiché ?
For i in range (10) :
	For j in range (10) :
		Print(‘ok’)

a)	20 fois	b ) 30 fois	c) 81 fois	d) 100 fois



17)	Combien de fois le mot ‘ok’ sera-t-il affiché ?
For i in range (10) :
	If i <=8: 
 		Print(‘ok’)

a)	7 fois	b ) 8 fois	c) 9 fois		d) 10 fois


18)	Combien de fois le mot ‘ok’ sera-t-il affiché ?
For i in range (1,4) :
	For j in range (i,4): 
 		Print(‘ok’)

a)	6 fois	b ) 8 fois	c) 10 fois	d) 16 fois

19)	Combien de fois le mot ‘ok’ sera-t-il affiché au maximum ?
From random import randint
For i in range (10) :
	Hazard= randint(1,10)
	If Hasard<=i: 
 		Print(‘ok’)

a)	5 fois	b ) 8 fois	c) 9 fois		d) 10 fois

20)	Soit la fonction suivante :
Def fonc(a,b) :
	Reste=a%b
	While reste>0 :
		a=b
		b=reste
		reste=a%b
	return (b)
Combien vaut fonc (48,30) ?
a)	0	b) 6	c)8	d)12
