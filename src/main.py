"""
LA IDEA VA A SER TENER UN EXCEL POR CADA MES, EN DONDE EN CADA WORKSHEET
VAYAN LOS DÍAS. LAS CATEGORIAS VAN A SER: CANTIDAD, TIPO, PRECIO, PERSONA, CATEGORÍA
PARA GARANTIZAR EL CORRECTO ORDEN.
LA IDEA DEL SCRIPT DE PYTHON VA A SER TENER UNA MEJOR VISUALIZACIÓN
DE LA INFORMACIÓN Y CALCULAR RÁPIDAMENTE LO QUE DEBE EL UNO AL OTRO.
ADEMÁS, SERÍA BUENO AÑADIR UN WORKSHEET DE GASTOS PERSONALES, QUE NO
VAYAN INCLUIDOS EN EL CÁLCULO FINAL, YA QUE SERÍA PERSONAL, VALGA LA
REDUNDANCIA.
ADEMÁS, SERÍA BUENO REPLICAR LAS MISMAS COLUMNAS EN TODOS LOS WORKSHEETS

"""

from functions import generador_archivos
from classes import LecturaArchivos

def main():
    numero = int(input("¿Que acción desea realizar?\n1) Crear un nuevo archivo\n2) Leer un archivo\n3) Visualizar los gastos no compartidos\n4) Gastos del mes\n"))
    
    if numero == 1:
        file = input("Ingresa como quieres guardar el archivo, ej: Marzo_2022.xlsx ")
        prim = int(input("Ingresa el primer día del mes "))
        fin = int(input("Ingresa el último día del mes "))
        mes = input("Ingresa el mes, ej: Marzo ")
        variable = generador_archivos(file, prim, fin, mes)
    
    elif numero == 2:
        nombre = input("Ingrese el nombre del archivo a leer, Ej: Marzo_2022.xlsx ")
        mes = input("Ingresa el mes del archivo: ")
        archivo = LecturaArchivos(nombre, mes)
        archivo.resumen_total()
        
    elif numero == 3:
        nombre = input("Ingrese el nombre de la persona que quiere revisar sus gastos personales:\nSolo se permite: Francisco o Felipe")
        archivo = input("Ingrese el nombre del archivo, ej: Marzo_2022.xlsx")
        mes = input("Ingresa el mes del archivo: ")
        lectura = LecturaArchivos(archivo, mes)
        lectura.gastos_unicos_persona(nombre)
   
    elif numero == 4:
       nombre = input("Ingrese el nombre del archivo a leer, Ej: Marzo_2022.xlsx ")
       mes = input("Ingresa el mes del archivo: ")
       archivo = LecturaArchivos(nombre, mes)
       archivo.gastos_totales_mes()

if __name__ == '__main__':
    main()
    