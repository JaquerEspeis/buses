#!/usr/bin/python3

import pyexcel
import csv

# Nota: Se cuenta iniciando en 0.

sheet = pyexcel.get_sheet(file_name="Tarifas_Autobus_2016-08-11_v3.xlsx", 
name_columns_by_row=1) 
# Le indico que los titulos están en las fila 1

titulos = list(sheet.colnames)

titulos_limpios = [ titulos[0],  # ruta
                    titulos[6],  # Descripción
                    titulos[14], # Empresa
                    titulos[15]] # info valiosa de empresa creo.


rows= pyexcel.to_array(sheet.rows())


# Extraigo la información que me interesa únicamente,
# además completo la información los puntos por donde pasa la ruta con info de
# la ruta.
def extrae_rutas(rows):
    rutas = []
    ultima_ruta = []
    for row in rows:
        # Hago algunas verificaciones para limpiar el código de las rutas
        # eliminadas y la columna de tarifa mínima que no interesa

        if len(row) >15 and row[6] != "" and row[6] != 'TARIFA MINIMA' \
         and  row[4] != 'Se elimina':
            if row[0] != "":
                ultima_ruta = [ row[0],
                                row[6],
                                row[14],
                                row[15]
                                ]
            elif ultima_ruta:
                # Es mejor si se repiten una y otra vez para los programas
                # de análisis
                rutas.append([
                    ultima_ruta[0],
                    row[6],
                    ultima_ruta[2],
                    ultima_ruta[3],
                ])
    return rutas



# Escribo el archivo csv con la información recopilada
with open('rutas.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter='\t',
                        quotechar='|', quoting=csv.QUOTE_MINIMAL)

    writer.writerow(titulos_limpios) # una fila 
    writer.writerows(extrae_rutas(rows)) # muchas filas la diferencia es la s (rows)


