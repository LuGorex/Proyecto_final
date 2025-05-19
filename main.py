import tkinter as tk
from mainwindowtk import MainWindow  # Importa la clase migrada a tkinter

if __name__ == "__main__":
    root = tk.Tk()  # Inicializa la ventana principal
    app = MainWindow(root)  # Crea una instancia de MainWindow

    # Llama al análisis semántico desde la raíz del árbol
    try:
        app.raiz.getInfo()  # Asegúrate de que 'raiz' sea la instancia de R0
    except Exception as e:
        print(f"Error durante el analisis semantico: {e}")

    root.mainloop()  # Inicia el bucle de eventos