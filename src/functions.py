from openpyxl.workbook import Workbook
import pandas as pd

def generador_archivos(nombre_archivo: str, primer_dia_mes: int, ultimo_dia_mes: int, mes: str) -> None:
    """
    ESTA FUNCIÓN SIRVE PARA GENERAR UN EXCEL QUE CONTIENE WORKSHEETS CON TODOS LOS DÍAS DEL MES
    """
    
    wb = Workbook()
    
    for i in range(primer_dia_mes, ultimo_dia_mes + 1):
        wb.create_sheet(f"{i} {mes}")
        
    wb.save(filename = f"{nombre_archivo}")
    
    
def generador_columnas():
    dataframe = pd.DataFrame(columns = ["Cantidad", "Tipo", "Precio", "Persona", "Categoría"])
    print(dataframe.head())