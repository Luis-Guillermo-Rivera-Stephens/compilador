from openpyxl import load_workbook

def escribir_en_excel(archivo, columna, valor):
    wb = load_workbook(archivo)
    hoja = wb.active

    fila = 2
    while hoja[f'{columna}{fila}'].value is not None:
        fila += 1
    

    hoja[f'{columna}{fila}'] = valor

    wb.save(archivo)
    return fila  