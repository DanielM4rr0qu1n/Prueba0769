import tkinter as tk
from tkinter import messagebox

# Función para la acción de asignación (puede ser personalizada)
def asignar_curso(nombre_curso):
    confirmacion = messagebox.askquestion("Confirmar", f"¿Estás seguro que te quieres asignar a {nombre_curso}?")

    if confirmacion == "yes":
        with open("Estudiantil.txt", "a") as archivo_estudiantil:
            archivo_estudiantil.write(f"Curso asignado: {nombre_curso}\n")
            messagebox.showinfo("Éxito", "La asignación se ha guardado la puedes visualizar en mis curos.")
    else:
        messagebox.showinfo("Cancelado", "La asignación ha sido cancelada.")

# Función para mostrar la información de los cursos y los botones de asignación
def mostrar_cursos():
    try:
        with open("catedratico.txt", "r") as archivo:
            contenido = archivo.read()
            cursos = contenido.split('\n\n')  # Separar cada curso

            for curso in cursos:
                info_curso = curso.split('\n')
                nombre_curso = info_curso[1].split(': ')[1]
                profesor = info_curso[0].split(': ')[1]
                descripcion = info_curso[2].split(': ')[1]

                # Mostrar la información del curso
                label_info = tk.Label(frame, text=f"Nombre: {nombre_curso}\nProfesor: {profesor}")
                label_info.pack(anchor="w")

                # Cuadro de texto para mostrar la descripción
                texto_descripcion = tk.Text(frame, height=4, width=40)
                texto_descripcion.insert(tk.END, descripcion)
                texto_descripcion.config(state=tk.DISABLED)  # Hacer el cuadro de texto de solo lectura
                texto_descripcion.pack(anchor="w")

                # Crear el botón de asignación para cada curso
                btn_asignar = tk.Button(frame, text="Asignación", command=lambda curso=nombre_curso: asignar_curso(curso))
                btn_asignar.pack(anchor="e")

                # Separador entre cursos
                separador = tk.Frame(frame, height=1, width=400, bg="grey")
                separador.pack(fill="x", pady=5)

    except FileNotFoundError:
        label_error = tk.Label(root, text="¡Archivo no encontrado!")
        label_error.pack()

# Configuración de la ventana principal
root = tk.Tk()
root.title("Cursos - Asignación")
root.geometry("600x600")  # Ajuste de las dimensiones de la ventana

# Crear una barra superior con color DeepSkyBlue2
barra_superior = tk.Frame(root, height=30, bg="DeepSkyBlue2")
barra_superior.pack(fill="x")

# Marco para la información de los cursos y los botones de asignación
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# Botón para mostrar la información de los cursos
btn_mostrar = tk.Button(root, text="Mostrar Cursos", command=mostrar_cursos)
btn_mostrar.pack()

# Botón para cerrar la ventana en la parte inferior derecha
btn_cerrar = tk.Button(root, text="Cerrar", command=root.destroy)
btn_cerrar.pack(side="bottom", anchor="se", padx=10, pady=10)

root.mainloop()