import tkinter as tk #Le doy un alias a la biblioteca
from tkinter import ttk #Importo ttk para mejores widgets
from tkinter import messagebox #Con esto importo las pestañas emergentes de mensajes y avisos.

#VENTANA
Principal = tk.Tk()
Principal.title("USAC - Inicio")
Principal.configure(bg="papayawhip")

#Ventana Centrada:
ancho_Ven_Prin = 1040 # Pongo el tamaño que busco de la ventana
alto_Ven_Prin = 640

ancho_pantalla = Principal.winfo_screenwidth() #Obtengo el ancho y alto de la pantalla con la información
alto_pantalla = Principal.winfo_screenheight() #Con .winfo encuentro la información de la pantalla en la que trabajo

x = (ancho_pantalla - ancho_Ven_Prin) // 2 #Calculo la posición para centrar la ventana en la pantalla
y = (alto_pantalla - alto_Ven_Prin) // 2 #Esto va en relación a los bordes al rededor de la ventana, de ahí la fórmula

Principal.geometry(f"{ancho_Ven_Prin}x{alto_Ven_Prin}+{x}+{y}") #Configuramos la geometría de la ventana para centrarla
#Acá se us "f" como una cadena formateada, perimite leer las {} en Python, esto hace que pueda sustituir esto luego por los valores que les asigné.

#Empiezan Funcionamientos
#Funciones
def contra_olvid():
    #Ventana
    Recuperar = tk.Toplevel(Principal)
    Recuperar.title("Recuperar Contraseña")
    
    ancho_Ven_fecha = 320 
    alto_Ven_fecha = 240

    ancho_pantalla = Recuperar.winfo_screenwidth() 
    alto_pantalla = Recuperar.winfo_screenheight() 
    
    xf = (ancho_pantalla - ancho_Ven_fecha) // 2
    yf = (alto_pantalla - alto_Ven_fecha) // 2

    Recuperar.geometry(f"{ancho_Ven_fecha}x{alto_Ven_fecha}+{xf}+{yf}") 

    Recuperar.configure(bg="papayawhip")
    
    #WIDGETS
    #Labels
    tit_fuent = ("Bahnschrift", 14)
    tit_label = tk.Label(Recuperar, text="Recuperar contraseña", bg="papayawhip", font=tit_fuent)
    info_label = tk.Label(Recuperar, text="Ingresa tu correo y luego se te mandará\n un correo con tu contraseña dentro.", bg="papayawhip")
    recu_label = tk.Label(Recuperar, text="E-mail:", bg="papayawhip")
    
    #Cuadros de Texto
    mail_recu = tk.Entry(Recuperar, width=50)
    
    #Botones
    send_mail = tk.Button(Recuperar, text="Enviar")
    
    #PACKS
    tit_label.pack(pady=(30, 5))
    info_label.pack(pady=(0, 5))
    recu_label.pack(pady=(0, 5))
    mail_recu.pack(pady=(0, 5))
    send_mail.pack(pady=(0, 5))
    
#Registrarse Alumno - Boton Registrarse

#FUnción para Inicio de Sesión.

#LOGO
Logo_icon = tk.PhotoImage(file="USAC_Logo.png") #Las cargo con tk.Photo, de la carpeta.

#LABELS
fuente_Titulo = ("Bahnschrift", 20) #Asigno una variable con el nombre y tamaño de la fuente.
Logo_label = tk.Label(Principal, image=Logo_icon, bg="papayawhip")
Inicio_label = tk.Label(Principal, text="Inicio de Sesión", bg="papayawhip", font=fuente_Titulo) #Label se refiere a información o cuadros descriptivos. Con tk.Label agrego el texto descriptivo. Con bg le agrego color al fondo.
Usario_label = tk.Label(Principal, text="Usuario:", bg="papayawhip")
Contraseña_label = tk.Label(Principal, text="Contraseña:", bg="papayawhip")
recu_contra_label = tk.Label(Principal, text="¿Has olvidado tu contraseña?", bg="papayawhip", fg="blue", cursor="hand2") #Acá cursor solo cambia el aspecto del mouse al pasar por esto.

espacio_label = tk.Label(Principal, text=" ", width=50, bg="papayawhip")

#BOTONES
Iniciar = tk.Button(Principal, text="Iniciar", width=20)
Registrar = tk.Button(Principal, text="Registrar", width=20)

#CUADROS TEXTO
usuario = tk.Entry(Principal, width=50)
contraseña = tk.Entry(Principal, width=50, show="*")

#PACKS
Logo_label.pack(pady=(70, 0))
Inicio_label.pack(pady=(20, 10))
Usario_label.pack(padx=(0, 260))
usuario.pack(pady=(0, 10))
Contraseña_label.pack(padx=(0, 240), pady=(5, 0))
contraseña.pack(pady=(0, 10))
recu_contra_label.pack(padx=(150, 0))
espacio_label.pack(side="left")
Iniciar.pack(side="left", padx=10)
Registrar.pack(side="left")

#CLICKS
recu_contra_label.bind("<Button-1>", lambda event: contra_olvid())

Principal.mainloop()