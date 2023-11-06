import tkinter as tk
from tkinter import messagebox

# Función para leer los datos de Estudiantil.txt y mostrar solo los nombres de los cursos
def mostrar_cursos():
    try:
        with open("Estudiantil.txt", "r") as file:
            cursos = [line.strip().replace("Curso asignado: ", "") for line in file.readlines()]
        return cursos
    except FileNotFoundError:
        messagebox.showerror("Error", "El archivo Estudiantil.txt no se ha encontrado.")

# Función para guardar las notas ingresadas en notas.txt
def guardar_notas(cursos, notas):
    try:
        with open("notas.txt", "w") as file:
            for i, curso in enumerate(cursos):
                nota = notas[i].get() if notas[i].get() else "0"
                nota = int(nota) if nota.isdigit() else 0  # Convertir a entero, si es posible
                nota = min(nota, 100)  # Establecer un máximo de 100
                file.write(f"{curso}    {nota}\n")
        messagebox.showinfo("Notas guardadas", "Notas guardadas con éxito en notas.txt")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudieron guardar las notas: {e}")

# Función para mostrar los datos de notas.txt en una nueva ventana
def mostrar_notas():
    try:
        with open("notas.txt", "r") as file:
            notas = file.read()

            notas_window = tk.Toplevel()
            notas_window.title("Notas guardadas")
            
            notas_text = tk.Text(notas_window)
            notas_text.insert(tk.END, notas)
            notas_text.pack()
    except FileNotFoundError:
        messagebox.showerror("Error", "El archivo notas.txt no se ha encontrado.")

# Función para cerrar la ventana
def cerrar_ventana(ventana):
    ventana.destroy()

# Función principal que crea la interfaz gráfica
def crear_interfaz():
    cursos = mostrar_cursos()

    if cursos:
        root = tk.Tk()
        root.title("Registro de Notas")

        barra_superior = tk.Frame(root, bg='DeepSkyBlue2', height=40)
        barra_superior.pack(fill='x')

        entradas_notas = []
        for curso in cursos:
            etiqueta = tk.Label(root, text=curso)
            etiqueta.pack()

            entrada_nota = tk.Entry(root)
            entrada_nota.pack()
            entradas_notas.append(entrada_nota)

        def guardar_y_mostrar_mensaje():
            guardar_notas(cursos, entradas_notas)
        
        boton_guardar = tk.Button(root, text="Guardar Notas", command=guardar_y_mostrar_mensaje)
        boton_guardar.pack()

        boton_ver_notas = tk.Button(root, text="Ver Notas", command=mostrar_notas)
        boton_ver_notas.pack(side='left', anchor='sw')
        
        boton_cerrar = tk.Button(root, text="Cerrar", command=lambda: cerrar_ventana(root))
        boton_cerrar.pack(side='bottom', anchor='se')

        root.geometry("500x500")
        root.mainloop()
    else:
        messagebox.showerror("Error", "No se encontraron cursos en el archivo Estudiantil.txt")

crear_interfaz()
