import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import subprocess

def abrir_C1():
    subprocess.run(["python", "Edit.py"])

def abrir_O1():
    subprocess.run(["python", "O.py"])

def main():
    # Crea una ventana de Tkinter
    window = tk.Tk()
    
    # Establece el título de la ventana
    window.title('Catedratico')
    
    # Establece el tamaño de la ventana
    window.geometry('500x500')

    window.configure(bg='white')

    # Crea una barra superior de color DeepSkyBlue2
    top_bar = tk.Frame(window, bg='DeepSkyBlue2', height=40)
    top_bar.pack(fill='x')

    # Crea un estilo personalizado para los botones
    style = ttk.Style()
    style.configure('TButton', background='PapayaWhip')

    # Crea los mosaicos (botones cuadrados) con el estilo personalizado
    tiles = ['Cursos','Notas',]
    
    for tile in tiles:
        frame = ttk.Frame(window, padding=10)
        frame.pack(fill='x')

        if tile == 'Cursos':
            button = ttk.Button(frame, text=tile, width=15, style="TButton", command=abrir_C1)
            button.pack(fill='x')
        elif tile == 'Notas':
            button = ttk.Button(frame, text=tile, width=15, style="TButton", command=abrir_O1)
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
