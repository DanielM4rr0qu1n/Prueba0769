import tkinter as tk
from tkinter import messagebox

def save_changes(profesores_text, cursos_text):
    profesores_data = profesores_text.get("1.0", tk.END)
    cursos_data = cursos_text.get("1.0", tk.END)

    with open("Data.txt", "w") as file:
        file.write(profesores_data)

    with open("cursos.txt", "w") as file:
        file.write(cursos_data)

    messagebox.showinfo("Éxito", "Cambios guardados con éxito.")  # Muestra el mensaje de éxito

def create_data_window():
    data_window = tk.Tk()
    data_window.title("Sección de Datos")
    data_window.geometry('500x500')
    data_window.configure(bg='white')

    top_bar = tk.Frame(data_window, bg='DeepSkyBlue2', height=40)
    top_bar.pack(fill='x')

    profesores_label = tk.Label(data_window, text="Editar Administradores, Profesores y Estudiantes")
    profesores_label.pack()

    profesores_text = tk.Text(data_window, height=10, width=60)
    profesores_text.pack()

    cursos_label = tk.Label(data_window, text="Editar Cursos")
    cursos_label.pack()

    cursos_text = tk.Text(data_window, height=10, width=60)
    cursos_text.pack()

    try:
        with open("Data.txt", "r") as file:
            profesores_info = file.read()
            profesores_text.insert(tk.END, profesores_info)

        with open("cursos.txt", "r") as file:
            cursos_info = file.read()
            cursos_text.insert(tk.END, cursos_info)
    except FileNotFoundError:
        profesores_text.insert(tk.END, "No se encontró la información.")
        cursos_text.insert(tk.END, "No se encontró la información.")

    save_button = tk.Button(data_window, text="Guardar cambios", command=lambda: save_changes(profesores_text, cursos_text))
    save_button.pack()

    close_button = tk.Button(data_window, text="Cerrar", command=data_window.destroy)
    close_button.pack(side='bottom', anchor='se', padx=10, pady=10)

    data_window.mainloop()

if __name__ == "__main__":
    create_data_window()
