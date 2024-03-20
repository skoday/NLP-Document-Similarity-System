import tkinter as tk
from tkinter import filedialog
import pandas as pd

class Interfaz(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Interfaz con Tkinter")
        self.geometry("600x400")

        # Selector de archivo CSV
        self.label_csv = tk.Label(self, text="Seleccionar archivo CSV:")
        self.label_csv.pack()

        self.button_select_csv = tk.Button(self, text="Seleccionar archivo", command=self.cargar_csv)
        self.button_select_csv.pack()

        # Espacio para ingresar texto
        self.label_text = tk.Label(self, text="Ingresar texto:")
        self.label_text.pack()

        self.text_input = tk.Text(self, height=5)
        self.text_input.pack()

        # Menús desplegables
        self.label_dropdowns = tk.Label(self, text="Seleccionar opciones:")
        self.label_dropdowns.pack()

        self.option_menu_1 = tk.OptionMenu(self, tk.StringVar(), "Opción 1", "Opción 2", "Opción 3")
        self.option_menu_1.pack(side=tk.LEFT)

        self.option_menu_2 = tk.OptionMenu(self, tk.StringVar(), "Opción 1", "Opción 2", "Opción 3")
        self.option_menu_2.pack(side=tk.LEFT)

        self.option_menu_3 = tk.OptionMenu(self, tk.StringVar(), "Opción 1", "Opción 2", "Opción 3")
        self.option_menu_3.pack(side=tk.LEFT)

        # Botón para enviar datos de los dropdowns
        self.button_send_dropdowns = tk.Button(self, text="Enviar opciones", command=self.enviar_dropdowns)
        self.button_send_dropdowns.pack()

        # Espacio para mostrar registros de DataFrame
        self.label_dataframe = tk.Label(self, text="Registros de DataFrame:")
        self.label_dataframe.pack()

        self.dataframe_display = tk.Text(self, height=10)
        self.dataframe_display.pack()

        # Botón para cargar otro archivo CSV
        self.button_load_another_csv = tk.Button(self, text="Cargar otro archivo CSV", command=self.cargar_otro_csv)
        self.button_load_another_csv.pack()

    def cargar_csv(self):
        filepath = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if filepath:
            df = pd.read_csv(filepath)
            self.mostrar_dataframe(df)

    def cargar_otro_csv(self):
        filepath = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if filepath:
            df = pd.read_csv(filepath)
            self.mostrar_dataframe(df)

    def mostrar_dataframe(self, df):
        self.dataframe_display.delete("1.0", tk.END)  # Limpiar el área de visualización
        self.dataframe_display.insert(tk.END, df.to_string(index=False))

    def enviar_dropdowns(self):
        opcion_1 = self.option_menu_1["textvariable"].get()
        opcion_2 = self.option_menu_2["textvariable"].get()
        opcion_3 = self.option_menu_3["textvariable"].get()

        print("Opción 1:", opcion_1)
        print("Opción 2:", opcion_2)
        print("Opción 3:", opcion_3)

if __name__ == "__main__":
    app = Interfaz()
    app.mainloop()
