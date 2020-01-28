# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 19:41:23 2020

@author: CEC
"""

import pandas as pd
titulos = pd.read_csv('E:/INSUMOS PYTHON/data/titles.csv')
print(titulos.head())
print("\n"*2)
elenco = pd.read_csv('E:/INSUMOS PYTHON/data/cast.csv', encoding='utf-8')
print(elenco.head(10))
# cuantas peliculas estan listadas en el dataframe d etitulos
print(len(titulos))


# Cual fue la primer pelicula hecha titulada "Romeo and Juliet" ?
print(titulos[titulos.title == "Romeo and Juliet"].sort_values('year').head(1))

#******************
# Listar todas las peliculas que contengan la palabra "Exorcist"
# ordenadas de la mas vieja a la mas reciente.
print(titulos[titulos.title.str.contains("Exorcist")].sort_values('year'))

# Cuantas peliculas fueron hechas en el año 1950?
print(len( titulos[titulos.year == 1950] ))
# Cuantas peliculas fueron hechas en el año 1970?
print(len( titulos[titulos.year == 1970] ))

# Cuantas peliculas fueron hechas de 1950 a 1959
print(len( titulos[ (titulos.year >= 1950) & (titulos.year <= 1959) ] ))
print(len( titulos[ titulos.year // 10 == 195] ))

# En que años alguna pelicula llamada "Batman" se presento
print(titulos[ titulos.title == "Batman"])

print(titulos[titulos.title == "Amor"].sort_values('year').head(1))

print(titulos[ titulos.year == 1973].head(1))

# Cuantos roles o papeles hubo en la pelicula "The Godfather"
# Cuantos roles o papeles hubo en la pelicula "The Godfather"
print(len( elenco[elenco.title == "The Godfather"] ))
# Cuantos papeles en la pelicula "The Godfather" no estan clasificados en algun valor "n"
c = elenco[elenco.title == "The Godfather"]
c = c[c.n.isnull()]
print(len( c ))
# Cuantos papeles en la pelicula "The Godfather" si estuvieron clasificados con un valor "n"
c = elenco[elenco.title == "The Godfather"]
c = c[c.n.notnull()]
print(len(c))
# Mostrar el elenco completo de la pelicula "2001: A Space Odyssey"
# ordenado por su clasificasión "n", ignorando los papeles que
# no se les asigno ningun valor "n"
c = elenco
c = c[c.title == "2001: A Space Odyssey"]
c = c[c.n.notnull()].sort_values('n')
print(c)
# Mostrar el elenco completo ordenado por la clasificacion "n"
# de la pelicula "Dracula" de 1958
c = elenco
c = c[ (c.title == "Dracula") & (c.year == 1958) ]
c = c.sort_values("n")
print (c)
# Cuantos papeles fueron listados en la pelicula "The Wizard of Oz" de 1939
c = elenco
c = c[ (c.title == "The Wizard of Oz") & (c.year == 1939) ]
print(len(c))
# Cuantos papeles de "Bruce Wayne" han sido hechos en la historia
# de las peliculas
c = elenco
c = c[c.character == "Bruce Wayne"]
print(len(c))
# Cuanta gente ah hecho el papel de "Romeo"
c = elenco
c = c[c.character == "Romeo"]
print(len(c))
# Cuantos papeles ah hecho "Robert De Niro" en su carrera
c = elenco
c = c[c.name == "Robert De Niro"]
print(len(c))
# Listado de papeles de soporte que tuvo el actor "Charlton Heston" en
# la decada de los 50's, ordenado por año
c = elenco
c = c[c.name == "Charlton Heston"]
c = c[c.n == 2]
c = c[c.year // 10 == 195]
c = c.sort_values('year')
print (c)
# Listado de papeles como protagonista que tuvo el actor "Charlton Heston" en
# la decada de los 60's, ordenado por año de forma descendente
c = elenco
c = c[c.name == "Charlton Heston"]
c = c[c.n == 1]
c = c[c.year // 10 == 196]
c = c.sort_values('year',ascending=False)
print (c)
# ¿Cuantos papeles para actores hubo en la decada de los 50's?
c = elenco
c = c[c.type == "actor"]
c = c[c.year //10 == 195]
print (len(c))
# ¿Cuantos papeles para actrices hubo en la decada de los 50's ?
c = elenco
c = c[c.type == "actress"]
c = c[c.year //10 == 195]
print(len(c))
# ¿Cuantos papeles protagonicos existen desde el principio de
# la historia filmatografica hasta 1970 ?
c = elenco
c = c[c.n == 1]
c = c[c.year <= 1970]
print (len(c))