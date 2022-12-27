#Escribir un programa que abra una ventana emergente de una calculadora totalmente funcional

import tkinter as tk

# Función para realizar las operaciones matemáticas
def calculate():
  # Obtenemos el valor de los campos de entrada
  num1 = float(entry1.get())
  num2 = float(entry2.get())

  # Realizamos la operación seleccionada
  if operator.get() == "Suma":
    result = num1 + num2
  elif operator.get() == "Resta":
    result = num1 - num2
  elif operator.get() == "Multiplicación":
    result = num1 * num2
  elif operator.get() == "División":
    result = num1 / num2
    
  # Mostramos el resultado en la etiqueta de resultado
  result_label.config(text=f"Resultado: {result}")

# Creamos la ventana principal
root = tk.Tk()
root.title("Calculadora")

# Creamos los campos de entrada para los números
entry1 = tk.Entry(root)
entry2 = tk.Entry(root)

# Creamos una lista de opciones para el menu desplegable
operations = ["Suma", "Resta", "Multiplicación", "División"]

# Creamos el menu desplegable para seleccionar la operación
operator = tk.StringVar(root)
operator.set(operations[0])
dropdown = tk.OptionMenu(root, operator, *operations)

# Creamos el botón de "Calcular"
button = tk.Button(root, text="Calcular", command=calculate)

# Creamos la etiqueta para mostrar el resultado
result_label = tk.Label(root)

# Colocamos todos los widgets en la ventana
entry1.pack()
entry2.pack()
dropdown.pack()
button.pack()
result_label.pack()

# Mostramos la ventana
root.mainloop()
