#!/usr/bin/python3
#! coding: utf-8


import math as m # Étend la gamme de fonctions disponibles en permettant l’usage de m.<fct> (par exemple : m.sin(x))
                             #et permet l’usage des constantes définies dans ce module..


tabPtSrc = [-5, -4, -3, -2, -1, 0, 1, 2, m.pi, 4, 5]
fct = input (“Saisissez la fonction f de x (en précisant tous les opérateurs) qui donne les images de “+str(tabPtSrc)+” : “)
print()
for i in tabPtSrc:
  try:
    fct_tmp = fct.replace(‘x’, str(i))
    print(“f(“+str(i)+”)=“, eval(fct_tmp))
  except:
    print()
--------------------------------------------------------------------------- Résultat --------------------------------------------------------------------------
Saisissez la fonction f de x (en précisant tous les opérateurs) qui donnent les images de [-5, -4, -3, -2, -1, 0, 1, 2, 3.141592653589793, 4, 5] : 4*x*x+m.sin(x)+2


f(-5)= 102.95892427466313
f(-4)= 66.75680249530792
f(-3)= 66.75680249530792
f(-2)= 66.75680249530792
f(-1)= 5.158529015192103
f(0)= 2.0
f(1)= 6.841470984807897
f(2)= 18.90929742682568
f(3.141592653589793)= 41.47841760435743
f(4)= 65.24319750469206
f(5)= 101.04107572533687