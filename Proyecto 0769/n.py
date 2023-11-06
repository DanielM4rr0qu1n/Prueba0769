import tkinter as tk
from tkinter import messagebox
import os

def desasignar_curso(curso, window):
    confirmacion = messagebox.askyesno("Confirmar", f"¿Estás seguro que deseas desasignar el curso {curso}?")
    if confirmacion:
        try:
            with open("Estudiantil.txt", "r") as file:
                lines = file.readlines()

            with open("Estudiantil_temp.txt", "w") as file_temp:
                for line in lines:
                    if f"Curso asignado: {curso}" not in line:
                        file_temp.write(line)
            
            os.remove("Estudiantil.txt")  # Elimina el archivo original
            os.rename("Estudiantil_temp.txt", "Estudiantil.txt")  # Renombra el archivo temporal como el original
            
            messagebox.showinfo("Éxito", f"El curso {curso} ha sido desasignado.")
        except FileNotFoundError:
            messagebox.showerror("Error", "El archivo Estudiantil.txt no se ha encontrado.")

def guardar_cambios(window):
    messagebox.showinfo("Guardado", "Cambios guardados exitosamente en Estudiantil.txt")
    window.destroy()  # Cerrar la ventana al guardar cambios

def mostrar_cursos_asignados():
    try:
        window = tk.Tk()
        window.title('Cursos Asignados')
        window.geometry("500x500")

        # Barra superior
        barra_superior = tk.Frame(window, bg='DeepSkyBlue2', height=40)
        barra_superior.pack(fill='x')

        with open("Estudiantil.txt", "r") as file:
            cursos = file.readlines()

        for curso in cursos:
            curso = curso.strip()
            frame = tk.Frame(window)
            frame.pack()

            label = tk.Label(frame, text=curso)
            label.pack(side="left")

            btn_desasignar = tk.Button(frame, text="Desasignar", command=lambda c=curso: desasignar_curso(c, window))
            btn_desasignar.pack(side="left")

        guardar_btn = tk.Button(window, text="Guardar Cambios", command=lambda: guardar_cambios(window))
        guardar_btn.pack()

        window.mainloop()
    except FileNotFoundError:
        messagebox.showerror("Error", "El archivo Estudiantil.txt no se ha encontrado.")

mostrar_cursos_asignados()
