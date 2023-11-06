import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import hashlib
import subprocess

cursos = []
profesores = []  # Lista para almacenar los profesores
profesores_disponibles = []  # Lista para los profesores disponibles

def abrir_ventana_datos():
    subprocess.Popen(["python", "d.py"])

def abrir_ventana_Listado():
    subprocess.Popen(["python", "e.py"])
    
def guardar_profesor(nombre, apellido, dpi, contraseña):
    # Encriptar la contraseña
    hashed_password = hashlib.sha256(contraseña.encode()).hexdigest()
    
    profesores.append({"nombre": nombre, "apellido": apellido, "dpi": dpi, "contraseña": hashed_password})
    
    # Guardar la información del profesor en data.txt
    with open("Data.txt", "r+") as file: #r+ es el modo lectura y escritura.
        contenido = file.read() #Acá leo el contenido que va dentro del archivo.
        file.seek(0) #Esto manda el mouse, bueno el selector para escribir al principio del archivo para sobreescribir el contenido.
        
        file.write(f"Tipo de Cuenta: Catedratico\n")
        file.write(f"Estado de Cuenta: Desbloqueado\n")
        file.write(f"Nombre: {nombre}\n")
        file.write(f"Apellido: {apellido}\n")
        file.write(f"DPI: {dpi}\n")
        file.write(f"Contrasena: {hashed_password}\n")
        file.write(f"--------------------------------\n")
        file.write(contenido) #Esto es para sobre escribir el contenido previo.
    
    actualizar_profesores_disponibles()    
    messagebox.showinfo("Realizado", "Profesor agregado con exito.")

def guardar_curso(nombre, precio, codigo, profesor, horario):
    cursos.append({"nombre": nombre, "precio": precio, "codigo": codigo, "profesor": profesor, "horario": horario})
    with open("cursos.txt", "a") as file:
        file.write(f"Nombre: {nombre}\nPrecio: {precio}\nCodigo: {codigo}\nProfesor: {profesor}\nHorario: {horario}\n\n")
    messagebox.showinfo("Éxito", "Curso agregado con éxito.")

def actualizar_profesores_disponibles():
    global profesores_disponibles
    profesores_disponibles = []
    
    try:
        with open("Data.txt", "r") as file:
            lines = file.readlines()
            
        current_profesor = {}
        for line in lines:
            line = line.strip()
            if line.startswith("Tipo de Cuenta: Catedratico"):
                current_profesor = {"Tipo de Cuenta": "Catedratico"}
            elif line.startswith("Estado de Cuenta: Desbloqueado"):
                current_profesor["Estado de Cuenta"] = "Desbloqueado"
            elif line.startswith("Nombre: "):
                current_profesor["Nombre"] = line.split(": ")[1]
            elif line.startswith("Apellido: "):
                current_profesor["Apellido"] = line.split(": ")[1]
            elif line == "--------------------------------":
                if "Tipo de Cuenta" in current_profesor:
                    profesores_disponibles.append(f"{current_profesor['Nombre']} {current_profesor['Apellido']}")
    except FileNotFoundError:
        messagebox.showerror("Error", "El archivo no se encuenta")

def create_window(window, title):
    new_window = tk.Toplevel(window)
    new_window.title(title)
    new_window.geometry('500x500')
    new_window.configure(bg='white')

    top_bar = tk.Frame(new_window, bg='DeepSkyBlue2', height=40)
    top_bar.pack(fill='x')

    return new_window

# Agregar curso con los datos ingresados
def agregar_curso(nombre, precio, codigo, profesor, horario, course_window):
    guardar_curso(nombre, precio, codigo, profesor, horario)
    messagebox.showinfo("Éxito", "Curso agregado con éxito.")
    actualizar_profesores_disponibles()
    course_window.destroy()

def gestion_cursos(window):
    def close_window(course_window):
        course_window.destroy()

    def open_course_window():
        course_window = create_window(window, "Agregar Curso")

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

        # Agrega un menú desplegable con los profesores disponibles
        profesor_selected = tk.StringVar(course_window)
        profesor_selected.set("")  # Valor inicial
        if profesores_disponibles:  # Si hay profesores disponibles
            profesor_option_menu = tk.OptionMenu(course_window, profesor_selected, *profesores_disponibles)
            profesor_option_menu.pack()
        else:
            messagebox.showinfo("Información", "No hay profesores disponibles. Agregue profesores primero.")

        horario_label = tk.Label(course_window, text="Horario:")
        horario_label.pack()
        horario_entry = tk.Entry(course_window)
        horario_entry.pack()

        agregar_button = tk.Button(course_window, text="Agregar Curso", command=lambda: agregar_curso(
            nombre_entry.get(), precio_entry.get(), codigo_entry.get(), profesor_selected.get(), horario_entry.get(), course_window
        ))
        agregar_button.pack()
        close_button = tk.Button(course_window, text="Cerrar", command=lambda: close_window(course_window))
        close_button.pack(side='bottom', anchor='se', padx=10, pady=10)
        
    open_course_window()

def agregar_profesor(nombre, apellido, dpi, contraseña, professor_window):
    hashed_password = hashlib.sha256(contraseña.encode()).hexdigest()
    
    with open("Data.txt", "a") as file:
        file.write(f"Tipo de Cuenta: Catedratico\n")
        file.write(f"Estado de Cuenta: Desbloqueado\n")
        file.write(f"Nombre: {nombre}\n")
        file.write(f"Apellido: {apellido}\n")
        file.write(f"DPI: {dpi}\n")
        file.write(f"Contrasena: {hashed_password}\n")
        file.write(f"--------------------------------\n")
    
    messagebox.showinfo("Éxito", "Profesor agregado con éxito.")
    professor_window.destroy()

def gestion_profesores(window):
    def close_window(professor_window):
        professor_window.destroy()

    def open_professor_window():
        professor_window = create_window(window, "Agregar Profesor")

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

        def validate_password():
            contraseña = password_entry.get()
            confirmar_contraseña = confirm_password_entry.get()
            mayuscula = any(c.isupper() for c in contraseña)
            minuscula = any(c.islower() for c in contraseña)
            numero = any(c.isdigit() for c in contraseña)
            longitud = len(contraseña) >= 8

            if contraseña == confirmar_contraseña and mayuscula and minuscula and numero and longitud:
                guardar_profesor(nombre_entry.get(), apellido_entry.get(), dpi_entry.get(), contraseña)
                messagebox.showinfo("Éxito", "Profesor agregado con éxito.")
                professor_window.destroy()
            else:
                mensaje_error = "Las contraseñas no coinciden o no cumplen con los requisitos:\n"
                if not (mayuscula and minuscula and numero and longitud):
                    mensaje_error += "- La contraseña debe tener al menos 8 caracteres, una mayúscula, una minúscula y un número.\n"
                if contraseña != confirmar_contraseña:
                    mensaje_error += "- Las contraseñas no coinciden."
                messagebox.showerror("Error", mensaje_error)

        agregar_button = tk.Button(professor_window, text="Agregar Profesor", command=validate_password)
        agregar_button.pack()

        close_button = tk.Button(professor_window, text="Cerrar", command=lambda: close_window(professor_window))
        close_button.pack(side='bottom', anchor='se', padx=10, pady=10)
        
    open_professor_window()

def cargar_profesores():
    # Carga la información de los profesores desde data.txt
    try:
        with open("Data.txt", "r") as file:
            lines = file.readlines() #En lista cada linea del txt
            profesores = [] #Esta es la lista en donde se almacenaran los profesores junto con sus datos.
            current_profesor = {} #Esto viene siendo cada profesor, acá se almacenan sus datos.
            
            for line in lines:
                line = line.strip() #recorre linea por linea del txt.
                if line == "Tipo de Cuenta: Catedratico": #Acá inspeccionamos que hay en cada linea y en base a eso lo almacenamos
                    current_profesor = {"Tipo de Cuenta": "Profesor"}
                elif line == "Estado de Cuenta: Desbloqueado":
                    current_profesor["Estado de Cuenta"] = "Desbloqueado"
                elif line.startswith("Nombre: "):
                    current_profesor["Nombre"] = line.split(": ")[1]
                elif line.startswith("DPI: "):
                    current_profesor["DPI"] = line.split(": ")[1]
                elif line.startswith("Contraseña: "):
                    current_profesor["Contraseña"] = line.split(": ")[1]
                elif line == "--------------------------------": #Esto indica el final de la info de cada profe
                    profesores.append(current_profesor)
            actualizar_profesores_disponibles()
            return profesores
    except FileNotFoundError:
        print("El archivo de profesores no se encuentra.")

def cargar_cursos():
    # Carga la información de los cursos desde cursos.txt
    try:
        with open("cursos.txt", "r") as file:
            lines = file.read().split('\n\n')  # Separa cada curso por líneas en blanco
            for line in lines:
                # Verifica si la línea no está vacía
                if line.strip():
                    course_info = line.strip().split('\n')
                    course_data = {}
                    for data in course_info:
                        key, value = data.split(': ')
                        course_data[key] = value
                    cursos.append(course_data)
    except FileNotFoundError:
        pass 

def main():
    # Cargar los datos existentes al iniciar la aplicación
    cargar_profesores()
    cargar_cursos()
    
    window = tk.Tk()
    window.title('Interfaz de Administrador')
    window.geometry('500x500')
    window.configure(bg='white')

    top_bar = tk.Frame(window, bg='DeepSkyBlue2', height=40)
    top_bar.pack(fill='x')

    style = ttk.Style()
    style.configure('TButton', background='PapayaWhip')

    tiles = ['Gestión de Usuarios', 'Gestión de Cursos', 'Gestión de Profesores', 'Datos',"Listado de profesores y cursos"]

    for tile in tiles:
        frame = ttk.Frame(window, padding=10)
        frame.pack(fill='x')

        if tile == 'Gestión de Usuarios':
            pass  # Puedes agregar la lógica para la gestión de usuarios aquí si es necesario
        elif tile == 'Gestión de Cursos':
            button = ttk.Button(frame, text=tile, width=15, style="TButton", command=lambda: gestion_cursos(window))
            button.pack(fill='x')
        elif tile == 'Gestión de Profesores':
            button = ttk.Button(frame, text=tile, width=15, style="TButton", command=lambda: gestion_profesores(window))
            button.pack(fill='x')
        elif tile == 'Datos':  # Cuando se presiona "Datos", llamará a abrir_ventana_datos
            button = ttk.Button(frame, text=tile, width=15, style="TButton", command=abrir_ventana_datos)
            button.pack(fill='x')
        elif tile == 'Listado de profesores y cursos':  # Cuando se presiona "Datos", llamará a abrir_ventana_datos
            button = ttk.Button(frame, text=tile, width=15, style="TButton", command=abrir_ventana_Listado)
            button.pack(fill='x')
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
    