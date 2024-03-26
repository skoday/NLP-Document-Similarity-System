import tkinter as tk
from tkinter import filedialog
import pandas as pd

def cargar_csv():
    filepath = filedialog.askopenfilename()
    if filepath:
        df = pd.read_csv(filepath)
        # Aquí puedes hacer lo que necesites con el DataFrame, como mostrarlo en una tabla o procesarlo de alguna manera

def enviar():
    # Aquí puedes obtener el texto del cuadro de texto y las selecciones de los menús desplegables y hacer lo que necesites con ellos
    opcion_1 = dropdown_1.get()
    opcion_2 = dropdown_2.get()
    opcion_3 = dropdown_3.get()
    texto = txt_input.get("1.0", tk.END)
    print("Opción 1:", opcion_1)
    print("Opción 2:", opcion_2)
    print("Opción 3:", opcion_3)
    print("Texto ingresado:", texto)

# Crear la ventana principal
root = tk.Tk()
root.title("Interfaz")

# Área para cargar archivo CSV y botón para procesarlo
frame_csv = tk.Frame(root)
frame_csv.pack(pady=10)
btn_cargar_csv = tk.Button(frame_csv, text="Cargar CSV", command=cargar_csv)
btn_cargar_csv.pack(side=tk.LEFT)
btn_procesar = tk.Button(frame_csv, text="Procesar")
btn_procesar.pack(side=tk.RIGHT)

# Cuadro de texto y menús desplegables
frame_inputs = tk.Frame(root)
frame_inputs.pack(pady=10)
txt_input = tk.Text(frame_inputs, width=50, height=5)  # Ajusta el número de filas según sea necesario
txt_input.pack(padx=5, side=tk.LEFT)

opciones_1 = ["Opción 1A", "Opción 1B", "Opción 1C"]
opciones_2 = ["Opción 2A", "Opción 2B", "Opción 2C"]
opciones_3 = ["Opción 3A", "Opción 3B", "Opción 3C"]

dropdown_1 = tk.StringVar(root)
dropdown_1.set(opciones_1[0])
menu_1 = tk.OptionMenu(frame_inputs, dropdown_1, *opciones_1)
menu_1.pack(padx=5, side=tk.LEFT)

dropdown_2 = tk.StringVar(root)
dropdown_2.set(opciones_2[0])
menu_2 = tk.OptionMenu(frame_inputs, dropdown_2, *opciones_2)
menu_2.pack(padx=5, side=tk.LEFT)

dropdown_3 = tk.StringVar(root)
dropdown_3.set(opciones_3[0])
menu_3 = tk.OptionMenu(frame_inputs, dropdown_3, *opciones_3)
menu_3.pack(padx=5, side=tk.LEFT)

# Botón de enviar
btn_enviar = tk.Button(root, text="Enviar", command=enviar)
btn_enviar.pack(pady=10)

# Ejecutar la aplicación
root.mainloop()
