import tkinter as tk
from tkinter import filedialog
import tkinter.ttk as ttk  # Importar ttk para widgets estilizados
import pandas as pd

class Interfaz(tk.Tk):
    def __init__(self):
        super().__init__()

        self.style = ttk.Style()  # Crear un objeto de estilo
        self.style.theme_use("clam")  # Aplicar un tema predefinido

        # --- Configuración general ---
        self.title("Interfaz Tkinter Estilizada")
        self.geometry("600x400")

        # --- Selector de archivo CSV ---
        self.label_csv = ttk.Label(self, text="Seleccionar archivo CSV:")
        self.label_csv.pack()

        self.button_select_csv = ttk.Button(self, text="Seleccionar archivo", command=self.cargar_csv)
        self.button_select_csv.pack()

        # --- Espacio para ingresar texto ---
        self.label_text = ttk.Label(self, text="Ingresar texto:")
        self.label_text.pack()

        self.text_input = tk.Text(self, height=5, width=40, borderwidth=2, relief="groove")  # Dar estilo al Text
        self.text_input.pack()

        # --- Menús desplegables ---
        self.label_dropdowns = ttk.Label(self, text="Seleccionar opciones:")
        self.label_dropdowns.pack()

        opciones = ["Opción 1", "Opción 2", "Opción 3"]
        variables = [tk.StringVar(value=opciones[0]) for _ in opciones]
        self.option_menus = [
            ttk.OptionMenu(self, variables[i], *opciones) for i in range(3)
        ]
        for menu in self.option_menus:
            menu.pack(side=tk.LEFT, padx=5)

        # --- Botón para enviar datos de los dropdowns ---
        self.button_send_dropdowns = ttk.Button(self, text="Enviar opciones", command=self.enviar_dropdowns)
        self.button_send_dropdowns.pack()

        # --- Espacio para mostrar registros de DataFrame ---
        self.label_dataframe = ttk.Label(self, text="Registros de DataFrame:")
        self.label_dataframe.pack()

        self.dataframe_display = tk.Text(self, height=10, width=50, borderwidth=2, relief="sunken")  # Dar estilo al Text
        self.dataframe_display.pack()

        # --- Botón para cargar otro archivo CSV ---
        self.button_load_another_csv = ttk.Button(
            self, text="Cargar otro archivo CSV", command=self.cargar_otro_csv
        )
        self.button_load_another_csv.pack()

        # --- Funciones de la interfaz ---
        # (El código de las funciones permanece igual)


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
