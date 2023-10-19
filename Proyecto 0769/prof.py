import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def main():
    # Crea una ventana de Tkinter
    window = tk.Tk()
    
    # Establece el título de la ventana
    window.title('Mi Aplicación GUI')
    
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
    tiles = [
        'Perfil',
        'Cursos',
        'Notas',
        'Designaciones'
    ]
    
    for tile in tiles:
        frame = ttk.Frame(window, padding=10)
        frame.pack(fill='x')
        
        # Haz que los botones sean cuadrados usando el padding y aplica el estilo personalizado
        button = ttk.Button(frame, text=tile, width=10, style="TButton")
        button.pack(fill='x')

    # Agrega un botón "Cerrar sesión" en la parte inferior derecha con el estilo personalizado
    logout_button = ttk.Button(window, text='Cerrar sesión', style="TButton", command=lambda: logout(window))
    logout_button.pack(side='bottom', anchor='se', padx=10, pady=10)

    # Inicia el bucle de eventos principal
    window.mainloop()

def logout(window):
    messagebox.showinfo("Información", "Sesión finalizada")
    window.destroy()

if __name__ == "__main__":
    main()

