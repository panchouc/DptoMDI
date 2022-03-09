"""
MI IDEA SERÍA LEER EL EXCEL, Y SER CAPAZ DE CALCULAR LO QUE LE DEBE EL UNO AL OTRO, LO QUE GASTO CADA UNO EN EL MES, ORDENAR SEGUN PRECIOS,
ORDENAR SEGÚN CATEGORÍAS, ORDENAR SEGUN PERSONAS.
FILTRAR SEGÚN LO MISMO QUE QUIERO ORDENAR
"""

import pandas as pd
from openpyxl.workbook import Workbook
from openpyxl import load_workbook


class LecturaArchivos:
    
    def __init__(self, nombre_archivo: str, mes: str) -> None:
        self.nombre = nombre_archivo
        self.mes = mes
        
    def resumen_total(self):
        """
        CALCULA LO QUE DEBE UNA PERSONA A LA OTRA, ADEMÁS DE RETORNAR UNA LISTA CON CIERTOS VALORES QUE PUEDEN SER DE INTERÉS
        """
        
        
        file = pd.ExcelFile(self.nombre)
        
        worksheets_names = []
        
        
        for i in file.sheet_names[:-1]:
            worksheets_names.append(pd.read_excel(file, i))
        
        result = pd.concat(worksheets_names[:-1])
        lista_resultados = result.iloc[:, :].values
        
        
        parcial_felipe = 0 #Gastos de felipe sin considerar los solo suyos
        parcial_francisco = 0 #Gastos de francisco sin considerar los solo suyos
        
        solo_felipe = 0 #Gastos totales de felipe
        solo_francisco = 0 #Gastos totales de francisco
        
        for i in lista_resultados:
            if i[3].capitalize() == "Felipe":
                parcial_felipe += int(i[2])
                
            elif i[3].capitalize() == "Francisco":
                parcial_francisco += int(i[2])
                
            elif i[3] == "Solo Felipe":
                solo_felipe += int(i[2])
            
            elif i[3] == "Solo Francisco":
                solo_francisco += int(i[2])
                
        print(f"TOTAL FELIPE: {parcial_felipe}, TOTAL FRANCISCO: {parcial_francisco}")
        print(f"FRANCISCO DEBE A FELIPE: {parcial_felipe / 2}")
        print(f"FELIPE DEBE A FRANCISCO: {parcial_francisco / 2}")
        
        print("RESUMEN DE CUENTAS")
        print("--------------------------------------------")
        
        if (parcial_felipe / 2) > (parcial_francisco / 2):
            print(f"FRANCISCO DEBE A FELIPE: {(parcial_felipe / 2) - (parcial_francisco)}")
        else:
            print(f"FELIPE DEBE A FRANCISCO: {(parcial_francisco / 2) - (parcial_felipe / 2)}")
            
        return [parcial_felipe, parcial_francisco, solo_felipe, solo_francisco]
       
    def gastos_unicos_persona(self, persona):
        
        """
        IMPRIME LOS GASTOS DE LA PERSONA, QUE NO SON COMPARTIDOS POR AMBOS
        """
        
        if persona == "Francisco":
            gastos_parciales = self.resumen_total()
            print(f"Los gastos SOLO de Francisco son: {gastos_parciales[3]}")
        
        elif persona == "Felipe":
            print(f"Los gastos SOLO de Felipe son: {gastos_parciales[2]}") 
               
    
    
    def gastos_totales_mes(self):
        file = pd.ExcelFile(self.nombre)
        
        
        worksheets_names = []
        
        for i in file.sheet_names:
            worksheets_names.append(pd.read_excel(file, i))
        
        result = pd.concat(worksheets_names)
    
        result.to_excel(f"Gastos totales {self.mes}.xlsx", index=False)