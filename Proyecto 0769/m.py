import tkinter as tk
from tkinter import messagebox, ttk

# Función para leer los cursos asignados del archivo Estudiantil.txt
def leer_cursos_asignados():
    cursos_asignados = []
    try:
        with open("Estudiantil.txt", "r") as file:
            cursos_asignados = file.readlines()
    except FileNotFoundError:
        messagebox.showerror("Error", "El archivo Estudiantil.txt no se ha encontrado.")
    return cursos_asignados

# Función para abrir un curso específico al hacer clic en el botón "Ingresar"
def abrir_curso_asignado(curso):
    messagebox.showinfo("Información", f"Ingresando al curso: {curso}")

# Función para mostrar los cursos asignados como mosaicos en la interfaz
def mostrar_cursos_asignados():
    cursos = leer_cursos_asignados()

    window = tk.Tk()
    window.title('Cursos Asignados como Mosaicos')
    window.geometry("500x500")  # Ajuste de las dimensiones de la ventana

    barra_superior = tk.Frame(window, height=30, bg="DeepSkyBlue2")
    barra_superior.pack(fill="x")

    container = ttk.Frame(window)
    container.pack(expand=True, padx=20, pady=20)

    cursos_frame = ttk.Frame(container)
    cursos_frame.pack(side="top")

    for curso_asignado in cursos:
        curso = curso_asignado.split(": ")[1].strip()

        curso_frame = ttk.Frame(cursos_frame, borderwidth=2, relief='ridge')
        curso_frame.pack(side='left', padx=10, pady=5)

        curso_label = ttk.Label(curso_frame, text=curso, font=('Arial', 12))
        curso_label.pack(padx=10, pady=5)

        abrir_curso = lambda c=curso: abrir_curso_asignado(c)
        btn_ingresar = ttk.Button(curso_frame, text="Ingresar", command=abrir_curso)
        btn_ingresar.pack(padx=10, pady=5)

    close_button = ttk.Button(window, text="Cerrar", command=window.destroy)
    close_button.pack(side='bottom', anchor='se', padx=10, pady=10)

    window.mainloop()

# Llamada a la función para mostrar los cursos asignados en la interfaz
mostrar_cursos_asignados()
