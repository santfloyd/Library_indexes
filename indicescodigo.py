# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal


gp = s1.groupby('Nombre_completo_au')
# groups() returns a dict with 'Gene':indices as k:v pair
for s in s1.groups.items():
    print(s1.loc[s[1]])
    
    Nombre_completo_au", sort=True)["Doc._No."]
   
    
    
    s2=df[["Doc._No.", "Nombre_completo_des"]]
for name, group in s2.groupby("Nombre_completo_des"):
    # print the name of the regiment
    print(name)
    # print the data of that regiment
    print(group) 
    
    
d = {k: g["Doc._No."].tolist() for k,g in s1.groupby("Nombre_completo_au")}
print(d)
"""

import pandas as pd
import collections

df=pd.read_excel('BaseSO_sutatenza(1).xlsx', 'Hoja1', na_values=[' '])
df=df[["Doc._No.","Autor_apellido","Autor_nombre", "Nombre_completo_au","Destinatario_apellido", "Destinatario_nombre", "Nombre_completo_des", "Lugar_elaboracion", "Ano", "Mes", "Dia", "Descripcion", "Folios"]]

#reducir
s1=df[["Doc._No.", "Nombre_completo_au"]]
#convertir int a object
s1["Doc._No."] = df["Doc._No."].astype(object)


#ordenar alfabéticamente
s1.sort()

#agrupar por nombre
for name, group in s1.groupby("Nombre_completo_au"):
    # print the name of the regiment
    print(name)
    # print the data of that regiment
    print(group)
#asegurarse que son del tipo object    
print s1.dtypes
#generar un diccionario con nombres unicos como key y los valores de la columna DOC.NO como 
#value solucion 1

#d = {k: g["Doc._No."].tolist() for k,g in s1.groupby("Nombre_completo_au")}
#print(d)

#solucion 2 con orden alfabètico
mydict = {}
for x in range(len(s1)):
    currentid = s1.iloc[x,1]
    currentvalue = s1.iloc[x,0]
    mydict.setdefault(currentid, [])
    mydict[currentid].append(currentvalue)
    mydict=collections.OrderedDict(sorted(mydict.items()))
print mydict
#escribe en el archivo 
with open("indices.txt", 'w') as f:
    for key, value in mydict.items():
        f.write('%s:%s\n' % (key, value))
