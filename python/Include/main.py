import openpyxl


# Crear un nuevo libro de Excel
wb = openpyxl.Workbook()
sheet = wb.active

# Encabezados
sheet["A1"] = "Nombre"
sheet["B1"] = "Clasificación"

# Diccionario para almacenar nombres y notas
estudiantes = {}

for i in range(3):
    nombre = input(f"Ingrese el nombre del estudiante {i+1}: ")
    
    while True:
        try:
            nota = float(input(f"Ingrese la nota de {nombre} (0.0 - 5.0): "))
            if 0.0 <= nota <= 5.0:
                break
            else:
                print(" Error: La nota debe estar entre 0.0 y 5.0.")
        except ValueError:
            print(" Error: Ingresa un número válido (ejemplo: 3.5).")

    estudiantes[nombre] = "Bueno" if nota > 3.5 else "Regular"

# Escribir en Excel
fila = 2
for nombre, clasificacion in estudiantes.items():
    sheet[f"A{fila}"] = nombre
    sheet[f"B{fila}"] = clasificacion
    fila += 1

# Guardar el archivo
wb.save("notas.xlsx")
print("✅ Archivo 'notas.xlsx' guardado correctamente.")
