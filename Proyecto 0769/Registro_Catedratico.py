import tkinter as tk #Le doy un alias a la biblioteca
from tkinter import ttk #Importo ttk para mejores widgets
from tkinter import messagebox #Con esto importo las pestañas emergentes de mensajes y avisos.

Ven_Prin = tk.Tk() #Con esto le asigno un alias a la "ventana principal"

Ven_Prin.title("Registro") #Asigno un titulo

#Ventana Centrada:
ancho_Ven_Prin = 1040 # Pongo el tamaño que busco de la ventana
alto_Ven_Prin = 640

ancho_pantalla = Ven_Prin.winfo_screenwidth() #Obtengo el ancho y alto de la pantalla con la información
alto_pantalla = Ven_Prin.winfo_screenheight() #Con .winfo encuentro la información de la pantalla en la que trabajo

x = (ancho_pantalla - ancho_Ven_Prin) // 2 #Calculo la posición para centrar la ventana en la pantalla
y = (alto_pantalla - alto_Ven_Prin) // 2 #Esto va en relación a los bordes al rededor de la ventana, de ahí la fórmula

Ven_Prin.geometry(f"{ancho_Ven_Prin}x{alto_Ven_Prin}+{x}+{y}") #Configuramos la geometría de la ventana para centrarla
#Acá se us "f" como una cadena formateada, perimite leer las {} en Python, esto hace que pueda sustituir esto luego por los valores que les asigné.

#Asigno color aunque de por si usaré el blanco.
Ven_Prin.configure(bg="papayawhip") #.config da varias opciones para modificar cosas como estetica, bg es para colores.

#Agrego un margen.
marco = tk.Frame(Ven_Prin) #Con tk.Frame añade el marco.
marco.pack(pady=70) #Añado el margen y le doy valores.

#Acá EMPIEZA CUADROS DE TEXTO
#Funciones para restringir cuadros de texto.
def val_num(Val):
    if not Val:
        return True
    elif Val == "DPI":
        return True
    elif Val.isdigit(): #Acá agrego un if, Val es solo un nombre que le doy, isdigit es lo que verifica si son numeros
        return True #Dando un valor verdadero si lo es, uno falso si no.
    else:
        messagebox.showerror("Error", "Ingresa números, tontito") #Acá saco la pestaña emergente con el mensaje que quiero.
        return False #Acá vuelvo el valor falso al no cumplirse.

def val_alpha(Val): #(Val) asigno el parametro con el que voy a trabajar o relacionar la función
    if not Val: #Esto permite al cuadro de texto estar en blanco, ya que no hay valores. Básicamente con el not significa que no hay nada y esto lo da como true para no saltar el error.
        return True #.replace es para los espacios. elif = "pero si también".
    elif Val.replace(" ", "").isalpha(): #isalnum, lo mismo pero con letras
        return True 
    else:
        messagebox.showerror("Error", "Ingresa letras, tontito") 
        return False

#Área de cuadros de texto.
#Funciones
#Guardar los datos en el archivo Data.
def guard_data(nombres, usuario, email, dpi, contraseña):
    with open("Data.txt", "a") as archivo: #open abre el archivo, "a" es para agregar.
        archivo.write(f"Tipo de cuenta: Catedratico\n")
        archivo.write(f"Nombre: {nombres}\n")
        archivo.write(f"Usuario: {usuario}\n")
        archivo.write(f"E-mail: {email}\n")
        archivo.write(f"DPI: {dpi}\n")
        archivo.write(f"Contrasena: {contraseña}\n")
        archivo.write("--------------------------------\n")
        
#Verificar contraseñas.
def verf_cont():
    contraseña = contra_usu.get() #Establezco variables
    Conf_contraseña = Conf_contra_usu.get()
    if contraseña == Conf_contraseña: #Determino si son o no iguales.
        return True #regreso valores falsos o verdaderos.
    else:
        messagebox.showerror("Error", "Las contraseñas no coinciden")
        return False
    
#función para llevar un registro, será útil cuando vaya a guardar todo en el txt.
def usu_uni(nickname_usu): #Esta función verificará que no se repita el usuario.
    with open("Data.txt", "r") as archivo:
        for line in archivo:
            if line.strip().startswith("Usuario:"):  # Busca líneas que comienzan con "Usuario:"
                existing_username = line.strip().split("Usuario: ")[1]
                if existing_username == nickname_usu:
                    return False  # El nombre de usuario ya existe en el archivo.
    return True  # El nombre de usuario es único.
#compará si el usuario ingresado ya existe en la lista que se lee en data.txt

#E-mail unico.
def mail_uni(email_usu): #creo la función y le asigno 1 argumento.
    with open("Data.txt", "r") as archivo: #con esto abro el txt en modo de lectura. Whit funciona como contexto solo para cerrarlo de forma correcta.
        for line in archivo: #Esto es un bucle para leer cada línea del archivo.
            if line.strip().startswith("E-mail:"): #Con .strip() elimino espacios y caracteres especiales al principio. Y con .startswith() encuentro la líea que empiece con E.mail.
                existing_mail = line.strip().split("E-mail: ")[1] #Acá separo la linea en 2 con .split, y existing_mail contendrá el e-mail existente.
                if existing_mail.strip() == email_usu: #Esto compara ambos e-mails.
                    return False #Si existe regresa un false.
    return True #Si no existen regresa un verdadero.

def grab_regis(): #acá creo una función la cuál usaré para darle sentido al botón de "registrar"
    if verf_cont():
        nombres = nom_usu.get() #Esto guarda en una variable el nombre obtenido por .get() del usuario.
        usuario = nickname_usu.get()
        email = email_usu.get()
        dpi = dpi_usu.get()
        contraseña = contra_usu.get()
        
        #Usuario único.
        if usu_uni(usuario):  # Pasamos una lista vacía como segundo argumento.
            if mail_uni(email):
                guard_data(nombres, usuario, email, dpi, contraseña)
                messagebox.showinfo("Registro Exitoso", "Tus datos han sido guardados exitosamente.")
                Ven_Prin.quit()
            else:
                messagebox.showerror("Error", "El e-mail ya esta en uso.")
        else:
            messagebox.showerror("Error", "El nombre de usuario ya existe.")
    
#Función para ocultar/mostrar Contraseña.
def bot_most_contra(): #defino la variable. cget selecciona un valor establecido de una variable para poder trabajar en él.
    if contra_usu.cget("show") == "*": #Acá se verifica si el contenido es "*", ósea, esta oculta.
        contra_usu.config(show="") #Esto genera el cambio de "*" a una cadena vacía, haría que se muestre la contra.
        bot_mostrar.config(image = mostrar_icon) #Esto hace que se muestre la imagen.
    else: 
        contra_usu.config(show="*") #Si la contra no era "*" significa que se ve, por lo que esto lo cambia "*".
        bot_mostrar.config(image = ocultar_icon)
        
#Acá haré funciones para eliminar el texto en el cuadro de texto
def texton_cuadros(event): #En este caso uso event para llamar la función cada que pase algo en especifico.
    if nom_usu.get() == "Nombre y Apellido": #Esto verifica que si salga el texto en el cuadro de texto.
        nom_usu.delete(0, tk.END) #Esto es lo que borra el texto. tk.END "hasta el final".
def textoe_cuadros(event):
    if email_usu.get() == "E-mail": 
        email_usu.delete(0, tk.END)
def textod_cuadros(event):
    if dpi_usu.get() == "DPI": 
        dpi_usu.delete(0, tk.END)
def textoNn_cuadros(event):
    if nickname_usu.get() == "Nombre de Usuario": 
        nickname_usu.delete(0, tk.END)
        
#Área de imagenes.
mostrar_icon = tk.PhotoImage(file="Mostrar.png") #Las cargo con tk.Photo, de la carpeta.
ocultar_icon = tk.PhotoImage(file="Oculto.png")

#Cuadros de texto.
nom_usu = tk.Entry(Ven_Prin, width=50, validate="key") #acá creo los cuadros de texto con tk.Entry
nom_usu.config(validate="key", validatecommand=(Ven_Prin.register(val_alpha), "%P")) #Uso .config para acceder a configuraciones de este widget, con validatecommand le doy chance a la función que creé antes de actuar, la cual es val_anum, %val son los datos que tengo dentro de ese cuadro de texto, Ven_Prin.register es para que la función pueda comunicarse de forma eficiente.
nickname_usu = tk.Entry(Ven_Prin, width=50)
email_usu = tk.Entry(Ven_Prin, width=50) #validate= es para validar y "key" significa que cuando se use el teclado.
dpi_usu = tk.Entry(Ven_Prin, width=50, validate="key")
dpi_usu.config(validate="key", validatecommand=(Ven_Prin.register(val_num), "%P"))
contra_usu = tk.Entry(Ven_Prin, width=50, show="*")
Conf_contra_usu = tk.Entry(Ven_Prin, width=50, show="*")

#Texto en los cuadros.
nom_usu.insert(0, "Nombre y Apellido") #con .insert agregamos el texto desde una posición inicial 0
nickname_usu.insert(0, "Nombre de Usuario")
email_usu.insert(0, "E-mail")
dpi_usu.insert(0, "DPI")

#Labels.
fuente_Titulo = ("Bahnschrift", 20) #Asigno una variable con el nombre y tamaño de la fuente.
CrearCuenta_label = tk.Label(Ven_Prin, text="Crear Nueva Cuenta ", bg="papayawhip", font=fuente_Titulo) #Label se refiere a información o cuadros descriptivos. Con tk.Label agrego el texto descriptivo. Con bg le agrego color al fondo.
    
#Boton de guardado y mostrar.
save_bot = tk.Button(Ven_Prin, text="Registrar", command=grab_regis, width=20) #Creo el boton con tk.Button, y le asigno la función que creé antes para guardar los datos ingresados. Con width configuro el largo.
bot_mostrar = ttk.Button(Ven_Prin, image=mostrar_icon, command=bot_most_contra)

#Ahora coloco todo en la ventana.
CrearCuenta_label.pack(padx=70, pady=(0, 5), anchor="w") #.pack hace que se ingresen uno debajo de otro.
nom_usu.pack(padx=70, pady=(0, 5), anchor="w") #con "pady=" lo muevo por megapixeles en y o x "padx"
nickname_usu.pack(padx=70, pady=(0, 5), anchor="w")
email_usu.pack(padx=70, pady=(0, 5), anchor="w")
dpi_usu.pack(padx=70, pady=(0, 5), anchor="w")
contra_usu.pack(padx=(70, 5), pady=(0, 5), anchor="w")
bot_mostrar.pack(padx=210, pady=(0,5), anchor="w")
Conf_contra_usu.pack(padx=70, pady=(0, 5), anchor="w")
save_bot.pack(padx=70, pady=(30, 0), anchor="w")

#Relacionar función de borrar textos con los cuadros.
nom_usu.bind("<Button-1>", texton_cuadros) #nombre es el a la variable que quiero asociar, .bind sirve para asociar eventos.
nickname_usu.bind("<Button-1>", textoNn_cuadros)
email_usu.bind("<Button-1>", textoe_cuadros) #<Button-1> representa el click izquierdo seguido de la función que a la que se le busca asociar.
dpi_usu.bind("<Button-1>", textod_cuadros)

Ven_Prin.mainloop()