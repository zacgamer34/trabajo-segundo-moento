import openpyxl

# Cargar el archivo Excel
wb = openpyxl.load_workbook("notas.xlsx")
sheet = wb.active  # Seleccionar la hoja activa

# Leer los datos e imprimirlos
print("\n📄 Datos del archivo 'notas.xlsx':\n")
for fila in sheet.iter_rows(values_only=True):  # Iterar sobre las filas
    print(f"{fila[0]:<15} | {fila[1]}")  # Imprimir en formato tabla
