import tkinter as tk
from tkinter import ttk, messagebox
import hashlib

def gestion_usuarios():
    def agregar_profesor():
        nombre = nombre_entry.get()
        apellido = apellido_entry.get()
        dpi = dpi_entry.get()
        password = password_entry.get()
        confirm_password = confirm_password_entry.get()

        if not (nombre and apellido and dpi and password and confirm_password):
            messagebox.showerror("Error", "Por favor, complete todos los campos.")
            return

        if password != confirm_password:
            messagebox.showerror("Error", "Las contraseñas no coinciden.")
            return

        # Validar que la contraseña cumpla con los requisitos
        if (
            len(password) < 8
            or not any(c.islower() for c in password)
            or not any(c.isupper() for c in password)
            or not any(c.isdigit() for c in password)
        ):
            messagebox.showerror("Error", "La contraseña debe tener al menos 8 caracteres y contener al menos una mayúscula, una minúscula y un número.")
            return

        # Encriptar la contraseña usando SHA-256
        password_hash = hashlib.sha256(password.encode()).hexdigest()

        with open("Data.txt", "a") as file:
            file.write(f"Nombre: {nombre}\n")
            file.write(f"Apellido: {apellido}\n")
            file.write(f"DPI: {dpi}\n")
            file.write(f"Contraseña encriptada: {password_hash}\n")
            file.write("\n")

        messagebox.showinfo("Éxito", "Profesor agregado con éxito.")
        professor_window.destroy()

    professor_window = tk.Toplevel()
    professor_window.title("Gestión de Usuarios")
    professor_window.geometry('500x500')  # Mismo tamaño que la ventana principal
    professor_window.configure(bg='white')

    top_bar = tk.Frame(professor_window, bg='DeepSkyBlue2', height=40)
    top_bar.pack(fill='x')

    nombre_label = tk.Label(professor_window, text="Nombre:")
    nombre_label.pack()
    nombre_entry = tk.Entry(professor_window)
    nombre_entry.pack()

    apellido_label = tk.Label(professor_window, text="Apellido:")
    apellido_label.pack()
    apellido_entry = tk.Entry(professor_window)
    apellido_entry.pack()

    dpi_label = tk.Label(professor_window, text="DPI:")
    dpi_label.pack()
    dpi_entry = tk.Entry(professor_window)
    dpi_entry.pack()

    password_label = tk.Label(professor_window, text="Contraseña:")
    password_label.pack()
    password_entry = tk.Entry(professor_window, show="*")
    password_entry.pack()

    confirm_password_label = tk.Label(professor_window, text="Confirmar Contraseña:")
    confirm_password_label.pack()
    confirm_password_entry = tk.Entry(professor_window, show="*")
    confirm_password_entry.pack()

    agregar_button = tk.Button(professor_window, text="Agregar Profesor", command=agregar_profesor)
    agregar_button.pack()

    close_button = tk.Button(professor_window, text="Cerrar", command=professor_window.destroy)
    close_button.pack(side='bottom', anchor='se', padx=10, pady=10)

def gestion_cursos(window):
    def agregar_curso():
        nombre = nombre_entry.get()
        precio = precio_entry.get()
        codigo = codigo_entry.get()
        profesor = profesor_entry.get()
        horario = horario_entry.get()

        if not nombre or not precio or not codigo or not profesor or not horario:
            messagebox.showerror("Error", "Por favor, complete todos los campos.")
            return

        with open("cursos.txt", "a") as file:
            file.write(f"Nombre del curso: {nombre}\n")
            file.write(f"Precio: {precio}\n")
            file.write(f"Código: {codigo}\n")
            file.write(f"Profesor: {profesor}\n")
            file.write(f"Horario: {horario}\n")
            file.write("\n")

        messagebox.showinfo("Éxito", "Curso agregado con éxito.")
        course_window.destroy()

    course_window = tk.Toplevel(window)
    course_window.title("Gestión de Cursos")
    course_window.geometry('500x500')  # Mismo tamaño que la ventana principal
    course_window.configure(bg='white')

    top_bar = tk.Frame(course_window, bg='DeepSkyBlue2', height=40)
    top_bar.pack(fill='x')

    nombre_label = tk.Label(course_window, text="Nombre del curso:")
    nombre_label.pack()
    nombre_entry = tk.Entry(course_window)
    nombre_entry.pack()

    precio_label = tk.Label(course_window, text="Precio:")
    precio_label.pack()
    precio_entry = tk.Entry(course_window)
    precio_entry.pack()

    codigo_label = tk.Label(course_window, text="Código:")
    codigo_label.pack()
    codigo_entry = tk.Entry(course_window)
    codigo_entry.pack()

    profesor_label = tk.Label(course_window, text="Profesor:")
    profesor_label.pack()
    profesor_entry = tk.Entry(course_window)
    profesor_entry.pack()

    horario_label = tk.Label(course_window, text="Horario:")
    horario_label.pack()
    horario_entry = tk.Entry(course_window)
    horario_entry.pack()

    agregar_button = tk.Button(course_window, text="Agregar Curso", command=agregar_curso)
    agregar_button.pack()

    close_button = tk.Button(course_window, text="Cerrar", command=course_window.destroy)
    close_button.pack(side='bottom', anchor='se', padx=10, pady=10)

def main():
    window = tk.Tk()
    window.title('Interfaz de Administrador')
    window.geometry('500x500')
    window.configure(bg='white')

    top_bar = tk.Frame(window, bg='DeepSkyBlue2', height=40)
    top_bar.pack(fill='x')

    style = ttk.Style()
    style.configure('TButton', background='PapayaWhip')

    tiles = ['Gestión de Usuarios', 'Gestión de Cursos', 'Estadísticas', 'Datos']

    for tile in tiles:
        frame = ttk.Frame(window, padding=10)
        frame.pack(fill='x')

        if tile == 'Gestión de Usuarios':
            button = ttk.Button(frame, text=tile, width=15, style="TButton", command=gestion_usuarios)
        elif tile == 'Gestión de Cursos':
            button = ttk.Button(frame, text=tile, width=15, style="TButton", command=lambda: gestion_cursos(window))
        else:
            button = ttk.Button(frame, text=tile, width=15, style="TButton")
        button.pack(fill='x')

    logout_button = ttk.Button(window, text='Cerrar sesión', style="TButton", command=lambda: logout(window))
    logout_button.pack(side='bottom', anchor='se', padx=10, pady=10)

    window.mainloop()

def logout(window):
    messagebox.showinfo("Información", "Sesión finalizada")
    window.destroy()

if __name__ == "__main__":
    main()