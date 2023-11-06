import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Función para leer la información del archivo cursos.txt y organizarla
def leer_cursos():
    cursos = {}
    with open("cursos.txt", "r") as file:
        lines = file.read().strip().split('\n\n')  # Separar por entradas de cursos
        for entry in lines:
            curso_info = {}
            for line in entry.split('\n'):
                key, value = line.split(': ')
                curso_info[key] = value
            nombre_curso = curso_info.get("Nombre")
            profesor = curso_info.get("Profesor")
            if profesor and nombre_curso:
                if profesor not in cursos:
                    cursos[profesor] = {}
                cursos[profesor][nombre_curso] = curso_info.get("Descripción", "")
    return cursos


# Función para guardar los cambios en el archivo catedratico.txt
# Función para guardar los cambios en el archivo catedratico.txt
def guardar_cambios(profesor, curso, descripcion, ventana):
    with open("catedratico.txt", "a") as file:
        file.write(f"Profesor: {profesor}\n")
        file.write(f"Nombre: {curso}\n")
        file.write(f"Descripción: {descripcion}\n\n")
    messagebox.showinfo("Éxito", "Los cambios se guardaron con éxito en catedratico.txt")
    ventana.destroy()  # Cierra la ventana después de guardar los cambios


# Función para editar la descripción del curso
def editar_descripcion(profesor, curso, descripcion_actual=""):
    ventana = tk.Toplevel()
    ventana.title(f"Edición de Curso - {curso}")

    label_profesor = ttk.Label(ventana, text=f"Profesor: {profesor}")
    label_profesor.pack()

    label_curso = ttk.Label(ventana, text=f"Curso: {curso}")
    label_curso.pack()

    label_descripcion_actual = ttk.Label(ventana, text=f"Descripción Actual: {descripcion_actual}")
    label_descripcion_actual.pack()

    texto_descripcion = tk.Text(ventana, height=10, width=40)
    texto_descripcion.pack()

    boton_actualizar = ttk.Button(ventana, text="Actualizar Datos",
                              command=lambda: guardar_cambios(profesor, curso, texto_descripcion.get("1.0", "end-1c"), ventana))
    boton_actualizar.pack()

# Función para manejar el clic en el botón "Ingresar" de un curso específico
def on_ingresar_click(profesor, curso, descripcion):
    editar_descripcion(profesor, curso, descripcion)

# Código para mostrar los cursos en la interfaz
def mostrar_cursos():
    data = leer_cursos()

    window = tk.Tk()
    window.title('Cursos como mosaicos')

    container = ttk.Frame(window)
    container.pack(expand=True, padx=20, pady=20)

    row = 0
    column = 0

    for profesor, cursos in data.items():
        label_profesor = ttk.Label(container, text=f'Profesor: {profesor}', font=('Arial', 12, 'bold'))
        label_profesor.grid(row=row, column=column, columnspan=2, pady=10)
        row += 1

        for curso, descripcion in cursos.items():
            curso_frame = ttk.Frame(container, borderwidth=2, relief='ridge')
            curso_frame.grid(row=row, column=column, padx=10, pady=5)

            curso_label = ttk.Label(curso_frame, text=f'Curso: {curso}', font=('Arial', 10))
            curso_label.pack(padx=10, pady=5)

            curso_button = ttk.Button(curso_frame, text="Ingresar",
                                     command=lambda p=profesor, c=curso, d=descripcion: on_ingresar_click(p, c, d))
            curso_button.pack(padx=10, pady=5)

            column += 1

        row += 1
        column = 0
    close_button = ttk.Button(window, text="Cerrar", command=window.destroy)
    close_button.place(relx=1, rely=1, anchor='se')

    window.mainloop()

# Llamada a la función para mostrar los cursos en la interfaz
mostrar_cursos()
