import tkinter as tk
from tkinter import ttk, messagebox
from colorama import init, Fore
import rules
from analyzer import analyze

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Análisis LR(1)")
        self.root.geometry("1000x600")
        self.root.configure(bg="#1E1E1E")  # Fondo oscuro

        # Crear la barra superior (menú)
        self.create_menu()

        # Crear la barra lateral (explorer)
        self.create_sidebar()

        # Crear el área principal (editor de texto y tabla de resultados)
        self.create_main_area()

        # Crear la barra de estado
        self.status_label = tk.Label(self.root, text="Listo", anchor="w", relief="sunken", bg="#007ACC", fg="white", font=("Segoe UI", 10))
        self.status_label.pack(side="bottom", fill="x")  # Barra de estado en la parte inferior

    def create_menu(self):
        # Barra superior (menú)
        menu_bar = tk.Frame(self.root, bg="#333", height=25)
        menu_bar.pack(side="top", fill="x")

        file_menu = tk.Label(menu_bar, text="File", fg="white", bg="#333", padx=10, font=("Segoe UI", 10))
        file_menu.pack(side="left")
        edit_menu = tk.Label(menu_bar, text="Edit", fg="white", bg="#333", padx=10, font=("Segoe UI", 10))
        edit_menu.pack(side="left")
        view_menu = tk.Label(menu_bar, text="View", fg="white", bg="#333", padx=10, font=("Segoe UI", 10))
        view_menu.pack(side="left")

    def create_sidebar(self):
        # Barra lateral (explorer)
        sidebar = tk.Frame(self.root, bg="#252526", width=200)
        sidebar.pack(side="left", fill="y")

        explorer_label = tk.Label(sidebar, text="EXPLORER", fg="white", bg="#252526", anchor="w", padx=10, font=("Segoe UI", 10, "bold"))
        explorer_label.pack(fill="x", pady=5)

        # Botón con el símbolo de Play
        compile_button = tk.Button(
            sidebar,
            text="▶",  # Símbolo de Play
            bg="#252526",
            fg="white",
            command=self.automata,
            relief="flat",
            font=("Segoe UI", 20, "bold")  # Aumenta el tamaño de la fuente
        )
        compile_button.pack(fill="x", pady=10)

    def create_main_area(self):
        # Crear un PanedWindow para dividir el área principal
        main_paned = tk.PanedWindow(self.root, orient="vertical", bg="#1E1E1E")
        main_paned.pack(fill="both", expand=True)

        # Editor de texto
        editor_frame = tk.Frame(main_paned, bg="#1E1E1E")
        self.text_edit = tk.Text(editor_frame, bg="#1E1E1E", fg="white", insertbackground="white", wrap="none", undo=True, font=("Consolas", 12))
        self.text_edit.pack(fill="both", expand=True, padx=5, pady=5)
        main_paned.add(editor_frame)  # Agregar el editor al PanedWindow

        # Tabla de resultados con scrollbars
        table_frame = tk.Frame(main_paned, bg="#1E1E1E")
        y_scrollbar = tk.Scrollbar(table_frame, orient="vertical")
        y_scrollbar.pack(side="right", fill="y")
        x_scrollbar = tk.Scrollbar(table_frame, orient="horizontal")
        x_scrollbar.pack(side="bottom", fill="x")

        self.table = ttk.Treeview(
            table_frame,
            columns=("Token", "Num", "Lexema"),
            show="headings",
            yscrollcommand=y_scrollbar.set,
            xscrollcommand=x_scrollbar.set
        )
        self.table.heading("Token", text="Token")
        self.table.heading("Num", text="Num")
        self.table.heading("Lexema", text="Lexema")

        # Configurar columnas redimensionables
        self.table.column("Token", width=150, anchor="center")
        self.table.column("Num", width=100, anchor="center")
        self.table.column("Lexema", width=200, anchor="center")

        self.table.pack(fill="both", expand=True)
        y_scrollbar.config(command=self.table.yview)
        x_scrollbar.config(command=self.table.xview)

        main_paned.add(table_frame)  # Agregar la tabla al PanedWindow

        # Estilo para la tabla
        style = ttk.Style()
        style.configure("Treeview", background="#1E1E1E", foreground="white", fieldbackground="#1E1E1E", font=("Segoe UI", 10))
        style.configure("Treeview.Heading", background="#007ACC", foreground="black", font=("Segoe UI", 10, "bold"))

    def automata(self):
        # Obtener el texto del editor
        cadena = self.text_edit.get("1.0", tk.END).strip() + "$"
        self.status_label.config(text="Compilando...")

        try:
            # Llamar a la función analyze
            elementos, resultado = analyze(cadena, self.table)  # Pasa self.table como argumento

            # Mostrar mensaje de resultado
            if resultado == "Cadena aceptada!":
                #messagebox.showinfo("Mensaje", resultado)
                breakpoint = cadena.index("$")
                cadena = cadena[:breakpoint]
            else:
                messagebox.showwarning("Mensaje", "Cadena rechazada!")

            # Limpiar la tabla
            for row in self.table.get_children():
                self.table.delete(row)

            # Insertar los resultados en la tabla
            for elemento in elementos:
                self.table.insert("", "end", values=(elemento['token'], elemento['num'], elemento['lexema']))

            # Actualizar barra de estado
            self.status_label.config(text=resultado)
        except Exception as e:
            messagebox.showerror("Error", f"Error: {str(e)}")
            self.status_label.config(text="Error")

if __name__ == "__main__":
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()
