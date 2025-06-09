import pandas as pd
import numpy as np


   
np.random.seed(281) 
   
personas = pd.DataFrame({"persona_id": range(1, 7), "hogar_id": [1, 1, 2, 2, 3, 3]}) 
   
compra = pd.DataFrame( 
     
{ 
"compra_id": range(10), 
"persona_id": np.random.choice(personas["persona_id"], size=10), 
"monto": np.round(np.random.normal(50, 10, size=10), 2), 
} 
) 
  
print("\nPersonas:\n") 
print(personas) 
print("\nHogares:\n") 
print(compra) 


#se muestra una tabla donde se muestre la suma de las compras de las perosnas y su se muestre su id del hogar
sumaCompras = compra.groupby("persona_id")["monto"].sum().reset_index()
mostrarCompras = pd.merge(personas, sumaCompras, on="persona_id", how="left")#el pd.merge se usa para unir las dos tablas, el on es la columna que se usa para unir las tablas y how es el tipo de union que se quiere hacer
print("\nSuma de compras por personas:\n")
print(mostrarCompras)

#se muestra una tabla donde se muestre la suma de las compras de los hogares y su id del hogar
mostrarHogar = compra.groupby("persona_id")["monto"].sum().reset_index()
mostrarHogar = pd.merge(personas, mostrarHogar, on="persona_id", how="left")
mostrarHogar = mostrarHogar.groupby("hogar_id")["monto"].sum().reset_index()#el.groupby se usa para agrupar los datos por la columna hogar_id y luego se usa la funcion sum para sumar los montos de las compras de cada hogar
mostrarHogar = pd.merge(mostrarHogar, personas[["hogar_id"]].drop_duplicates(), on="hogar_id", how="left")#el .drop_duplicates se usa para eliminar los duplicados de la columna hogar_id
print("\nSuma de compras por hogares:\n")
print(mostrarHogar)


#se muestra una tabla donde se divide el monto de las compras por el numero de hogares por el numero de personas que lo conforman
promedioCompras = mostrarHogar["monto"] / personas.groupby("hogar_id")["persona_id"].count().values
promedioCompras = pd.DataFrame({"hogar_id": mostrarHogar["hogar_id"], "promedio_monto": promedioCompras})
print("\nPromedio de compras realizadas por hogar:\n")
print(promedioCompras)




