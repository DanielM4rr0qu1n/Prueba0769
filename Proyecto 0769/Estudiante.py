import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import subprocess

def abrir():
    subprocess.run(["python", "C.py"])

def abrir_cursos():
    subprocess.run(["python", "m.py"])

def eliminar_cursos():
    subprocess.run(["python", "n.py"])

def Notas():
    subprocess.run(["python", "notas.py"])

def main():
    # Crea una ventana de Tkinter
    ventana_principal = tk.Tk()
    
    # Establece el título de la ventana
    ventana_principal.title('Interfaz Estudiante')
    
    # Establece el tamaño de la ventana
    ventana_principal.geometry('500x500')

    # Crea una barra superior de color Coral
    barra_superior = tk.Frame(ventana_principal, bg='DeepSkyBlue2', height=40)
    barra_superior.pack(fill='x')

    # Configura el estilo para los botones
    estilo = ttk.Style()
    estilo.configure('BotonEstilizado.TButton', background='lightblue')  # Define el estilo para el botón

    # Crea los mosaicos (botones cuadrados) con el estilo personalizado
    mosaicos = [
        'Asignaciones',
        'Desasignación',
        'Cursos',
        'Notas'
    ]
    
    for tile in mosaicos:
        frame = ttk.Frame(ventana_principal, padding=10)
        frame.pack(fill='x')

        if tile == 'Asignaciones':  
            button = ttk.Button(frame, text=tile, width=15, style="TButton", command=abrir)  
            button.pack(fill='x')
        elif tile == 'Cursos':  
            button = ttk.Button(frame, text=tile, width=15, style="TButton", command=abrir_cursos)
            button.pack(fill='x')
        elif tile == 'Desasignación':  
            button = ttk.Button(frame, text=tile, width=15, style="TButton", command=eliminar_cursos)
            button.pack(fill='x')
        elif tile == 'Notas':  
            button = ttk.Button(frame, text=tile, width=15, style="TButton", command=Notas)
            button.pack(fill='x')
        else:
            button = ttk.Button(frame, text=tile, width=15, style="TButton")
            button.pack(fill='x')


    # Agrega un botón "Desconectar" en la parte inferior derecha con el estilo personalizado
    boton_desconectar = ttk.Button(ventana_principal, text='Cerrar', style="BotonEstilizado.TButton", command=lambda: desconectar(ventana_principal))
    boton_desconectar.pack(side='bottom', anchor='se', padx=10, pady=10)

    # Inicia el bucle de eventos principal
    ventana_principal.mainloop()

def desconectar(ventana):
    messagebox.showinfo("Información", "Sesión cerrada")
    ventana.destroy()

if __name__ == "__main__":
    main()
