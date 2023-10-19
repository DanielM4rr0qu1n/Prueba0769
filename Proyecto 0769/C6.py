import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Función para agregar cursos desde el archivo de texto
def agregar_curso(nombre, descripcion):
    with open("cursos.txt", "a") as file:
        file.write(f"{nombre}\n{descripcion}\n\n")

# Función para cargar cursos desde el archivo de texto
def cargar_cursos_disponibles():
    cursos = []
    with open("cursos.txt", "r") as file:
        lines = file.read().split("\n\n")
        for course_info in lines:
            course_info = course_info.strip().split("\n")
            if len(course_info) == 2:
                nombre, descripcion = course_info
                cursos.append((nombre, descripcion))
    return cursos

# Función para asignarse a un curso
def asignarse_a_curso(curso_id):
    cursos_asignados.append(curso_id)
    messagebox.showinfo("Asignación", f"¡Te has asignado al curso {curso_id}!")

# Función para mostrar la ventana de cursos asignados
def mostrar_cursos_asignados():
    ventana_cursos_asignados = tk.Toplevel()
    ventana_cursos_asignados.title("Cursos Asignados")

    for curso_id in cursos_asignados:
        curso_info = cursos_disponibles[curso_id - 1]
        curso_nombre, curso_descripcion = curso_info
        label = tk.Label(ventana_cursos_asignados, text=f"Curso: {curso_nombre}", font=("Arial", 12))
        label.pack()
        descripcion_label = tk.Label(ventana_cursos_asignados, text=f"Descripción: {curso_descripcion}", font=("Arial", 10))
        descripcion_label.pack()

# Crear ventana de estudiante
def ventana_estudiante():
    ventana_est = tk.Toplevel()
    ventana_est.title("Ventana de Estudiante")

    for i, curso_info in enumerate(cursos_disponibles):
        curso_nombre, _ = curso_info
        curso_button = tk.Button(ventana_est, text=f"Curso: {curso_nombre}", command=lambda id=i + 1: asignarse_a_curso(id))
        curso_button.pack()

# Configuración de la ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Cursos en Línea")
ventana_principal.configure(bg="papayawhip")

cursos_asignados = []  # Lista para almacenar los cursos asignados
cursos_disponibles = cargar_cursos_disponibles()

# Barra superior con fondo azul
barra_superior = tk.Frame(ventana_principal, bg="blue")
barra_superior.pack(fill="x")

# Obtener el nombre del usuario
nombre_usuario = ""

# Etiqueta para mostrar el nombre de usuario
usuario_label = tk.Label(barra_superior, text=f"Bienvenido, {nombre_usuario}", font=("Arial", 12), bg="blue", fg="white")
usuario_label.pack(side="right", padx=10, pady=10)

# Margen en blanco en la parte superior
margen_superior = tk.Frame(ventana_principal, bg="white", height=20)
margen_superior.pack(fill="x")

# Botón "Mis cursos"
mis_cursos_button = tk.Button(ventana_principal, text="Mis cursos", font=("Arial", 14), bg="blue", fg="white", command=mostrar_cursos_asignados)
mis_cursos_button.pack(pady=10)

# Margen en blanco en la parte media
margen_medio = tk.Frame(ventana_principal, bg="white", height=20)
margen_medio.pack(fill="x")

# Crear mosaicos
mosaicos_frame = tk.Frame(ventana_principal, bg="white")
mosaicos_frame.pack()

# Lista de nombres de mosaico
nombres_mosaico = [
    "Asignaciones",
    "Mosaico 2",
    "Mosaico 3"
]

# Lista de descripciones de mosaicos
descripcion_mosaicos = [
    "Asignarse a cursos disponibles",
    "Descripción del Mosaico 2",
    "Descripción del Mosaico 3"
]

# Tamaño de imagen de mosaico
tamaño_imagen_mosaico = (150, 150)

# Crear mosaicos
for i in range(len(nombres_mosaico)):
    mosaico = ttk.Frame(mosaicos_frame, padding=10)
    mosaico.grid(row=i // 3, column=i % 3, padx=20, pady=10)

    nombres_mosaico_label = tk.Label(mosaico, text=nombres_mosaico[i], font=("Arial", 12), bg="white", fg="blue")
    nombres_mosaico_label.pack()

    descripcion_mosaico_label = tk.Label(mosaico, text=descripcion_mosaicos[i], font=("Arial", 10), bg="white", fg="blue")
    descripcion_mosaico_label.pack()

    if i == 0:  # Si es el primer mosaico (Asignaciones)
        boton_mosaico = tk.Button(mosaico, text=f"Ir a {nombres_mosaico[i]}", font=("Arial", 10), bg="blue", fg="white", command=ventana_estudiante)
    else:
        boton_mosaico = tk.Button(mosaico, text=f"Ir a {nombres_mosaico[i]}", font=("Arial", 10), bg="blue", fg="white")

    boton_mosaico.pack()

ventana_principal.mainloop()
