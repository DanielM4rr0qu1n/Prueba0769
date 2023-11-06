import tkinter as tk #Le doy un alias a la biblioteca
from tkinter import ttk #Importo ttk para mejores widgets
from tkinter import messagebox #Con esto importo las pestañas emergentes de mensajes y avisos.
import os #Para variables de entorno.
from dotenv import load_dotenv
from email.message import EmailMessage #para el correo.
import ssl #Para mandarlo de forma segura en el servidor de gmail.
import smtplib
import re
import hashlib
import tkinter.filedialog
from PIL import Image, ImageTk
import subprocess
import cv2
import numpy as np

#VENTANA
Principal = tk.Tk()
Principal.title("USAC - Inicio")
Principal.configure(bg="white")

#Ventana Centrada:
ancho_Ven_Prin = 1040 # Pongo el tamaño que busco de la ventana
alto_Ven_Prin = 640

ancho_pantalla = Principal.winfo_screenwidth() #Obtengo el ancho y alto de la pantalla con la información
alto_pantalla = Principal.winfo_screenheight() #Con .winfo encuentro la información de la pantalla en la que trabajo

x = (ancho_pantalla - ancho_Ven_Prin) // 2 #Calculo la posición para centrar la ventana en la pantalla
y = (alto_pantalla - alto_Ven_Prin) // 2 #Esto va en relación a los bordes al rededor de la ventana, de ahí la fórmula

Principal.geometry(f"{ancho_Ven_Prin}x{alto_Ven_Prin}+{x}+{y}") #Configuramos la geometría de la ventana para centrarla
#Acá se us "f" como una cadena formateada, perimite leer las {} en Python, esto hace que pueda sustituir esto luego por los valores que les asigné.

mostrar_icon = tk.PhotoImage(file="Mostrar.png") #Las cargo con tk.Photo, de la carpeta.
ocultar_icon = tk.PhotoImage(file="Oculto.png")

#Empiezan Funcionamientos
#Funciones
contra_recu = None
mail_recu = None
def contra_olvid():
    global mail_recu
    global contra_recu
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

    Recuperar.configure(bg="white")
    
    #Funciones
    def enviar_correo(correo, contrasena):
        try:
            load_dotenv()
            #Variables con los datos del remitente y el receptor.
            
            contraseña_encriptada = hashlib.sha256(contrasena.encode()).hexdigest()
            
            email_sender = "edusac446@gmail.com"
            Password = os.getenv("PASSWORD") #La contraseña que con la libreria os la extraemos del archivo .env (como variable de entorno)
            email_reciver = "danimarroquin.1@gmail.com"
            #Subject=asunto    Body=cuerpo
            subject = "Recuperación de contraseña"
            body = f"El usuario con problemas es {correo} y su nueva contraseña es {contraseña_encriptada}"
            #Acá creo el email
            
            em = EmailMessage() #em es la variable en donde esta el correo que armé.
            em["From"] = email_sender
            em["To"] = email_reciver
            em["Subject"] = subject
            em.set_content(body)

            #PAra enviarlo de forma segura.
            context = ssl.create_default_context() #Lo usaré para mandar el correo
            #Esto es para ingresar al servidor de gmail.
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context = context) as smtp: 
                smtp.login(email_sender, Password) #Acá me logueo, primero usuario luego contra.
                smtp.sendmail(email_sender, email_reciver, em.as_string()) #Acá mando el correo. Remitente -> Receptor
                            
        except smtplib.SMTPAuthenticationError as e: #Esto si hay errores con inicios de sesión y así
            messagebox.showerror("Error", "Ha ocurrido un problema al enviar el correo.")
    
    def es_correo_valido(correo):
        # Patrón de expresión regular para validar correos electrónicos
        patron_correo = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(patron_correo, correo) is not None
    
    def recuperar_contrasena():
        global contra_recu
        correo = mail_recu.get() #Obtener el correo ingresado.
        contrasena_nueva = contra_recu.get() #obtener contraseña nueva ingresada.
        
        # Validar el formato del correo electrónico
        if not es_correo_valido(correo):
            messagebox.showerror("Error", "El formato del correo electrónico no es válido.")
            return  # Salir de la función si el formato es inválido
        
        with open("Data.txt", "r") as archivo: #abro el txt en lectura
            datos = archivo.readlines() #Lee todas las lineas de un archivo y las mete en una lista.

        usuario_encontrado = False #Valores a variables

        for i in range(len(datos)): #Con for recorremos todos los valores de la lista, poniendo un rango desde el inicio hasta el final.
            if datos[i].strip() == f"E-mail: {correo}": #el strip elimina espacios en blanco, y acá comparamos los datos hasta encontrar E-mail, si es el caso existe el correo.
                usuario_encontrado = True #Esto indica que se encontró y cierra los bucles
                break

        if usuario_encontrado:
            enviar_correo(correo, contrasena_nueva)
            messagebox.showinfo("Recuperar Contraseña", "Se ha enviado un correo al administrador")
            Recuperar.destroy()
        else:
            messagebox.showerror("Error", "El correo no se encontró en la base de datos.")

    
    #WIDGETS
    #Labels
    tit_fuent = ("Bahnschrift", 14)
    tit_label = tk.Label(Recuperar, text="Recuperar contraseña", bg="white", font=tit_fuent)
    info_label = tk.Label(Recuperar, text="Ingresa tu correo y nueva contraseña,\n el administrador se comunicará contigo", bg="white")
    recu_label = tk.Label(Recuperar, text="E-mail:", bg="white")
    recu_contra_label = tk.Label(Recuperar, text="Contraseña:", bg="white")
    
    #Cuadros de Texto
    mail_recu = tk.Entry(Recuperar, width=50)
    contra_recu = tk.Entry(Recuperar, width=50)
    
    #Botones
    send_mail = tk.Button(Recuperar, text="Enviar", command=recuperar_contrasena)
    
    #PACKS
    tit_label.pack(pady=(30, 5))
    info_label.pack(pady=(0, 5))
    recu_label.pack(pady=(0, 5))
    mail_recu.pack(pady=(0, 5))
    recu_contra_label.pack(pady=(0, 5))
    contra_recu.pack(pady=(0, 5))
    send_mail.pack(pady=(0, 5))
    
#Registrarse Alumno - Boton Registrarse
def registrar():
    Ven_Prin = tk.Toplevel() #Con esto le asigno un alias a la "ventana principal"

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
    Ven_Prin.configure(bg="white") #.config da varias opciones para modificar cosas como estetica, bg es para colores.

    #Agrego un margen.
    marco = tk.Frame(Ven_Prin) #Con tk.Frame añade el marco.
    marco.pack(pady=10) #Añado el margen y le doy valores.

    #Acá EMPIEZA CUADROS DE TEXTO
    #Funciones para restringir cuadros de texto.
    def val_num(Val):
        if not Val:
            return True
        elif Val == "Telefono": #Acá agrego a las función el texto para que lo admita sin tirar el cuadro de error ya que solo debería aceptar datos numericos
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
    def guard_data(nombres, usuario, email, telf, dpi, fecha, nombre_archivo, contraseña):
        with open("Data.txt", "a") as archivo: #open abre el archivo, "a" es para agregar.
            
            #Encriptar contra
            contraseña_encriptada = hashlib.sha256(contraseña.encode()).hexdigest()
            
            archivo.write(f"Tipo de Cuenta: Alumno\n")
            archivo.write(f"Estado de Cuenta: Desbloqueado\n")
            archivo.write(f"Nombre: {nombres}\n")
            archivo.write(f"Usuario: {usuario}\n")
            archivo.write(f"E-mail: {email}\n")
            archivo.write(f"Telefono: {telf}\n")
            archivo.write(f"DPI: {dpi}\n")
            archivo.write(f"Fecha de Nacimiento: {fecha}\n")
            archivo.write(f"Imagen: Image_Users/{nombre_archivo}\n")
            archivo.write(f"Contrasena: {contraseña_encriptada}\n")
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
        return True #Si no existen regresa un verdadero.}
    
    #Función para como debe ser la contraseña.
    def validar_contra(contraseña): #len sirver para contar el numero de caractores, verificando que esta tenga 8 o más.
        if len(contraseña) >= 8 and re.search(r"[A-Z]", contraseña) and re.search(r"\d", contraseña) and re.search(r"[!@#$%^&*(),.?\":{}|<>]", contraseña): #\d = [0-9]
            #El re.search se encarga de buscar que haya por lo menos 1 de los datos puestos.
            #r interpreta la cadena como raw (sin procesar), para que no tome valores especiales.
            return True #Si todo se cumple es verdad.
        else:
            return False #Si no es falso.
        
    nombre_archivo = None
    def grab_regis(): #acá creo una función la cuál usaré para darle sentido al botón de "registrar"
        global nombre_archivo
        if verf_cont():
            nombres = nom_usu.get() #Esto guarda en una variable el nombre obtenido por .get() del usuario.
            usuario = nickname_usu.get()
            email = email_usu.get()
            telf = telf_usu.get()
            dpi = dpi_usu.get()
            fecha = bot_fec.cget("text") #cget para obtener los valores de bot_fec
            contraseña = contra_usu.get()
            confirmacion_contra = Conf_contra_usu.get()
            
            #Confirmar contra
            if validar_contra(contra_usu.get()):
                if contraseña == confirmacion_contra:
                    #Usuario único.
                    if usu_uni(usuario) and mail_uni(email):
                        guardar_foto()
                        guard_data(nombres, usuario, email, telf, dpi, fecha, nombre_archivo, contraseña)
                        messagebox.showinfo("Registro Exitoso", "Tus datos han sido guardados exitosamente.")
                        Ven_Prin.destroy()  # Cierra la ventana de registro solo cuando el registro es exitoso
                    else:
                        if not usu_uni(usuario):
                            messagebox.showerror("Error", "El nombre de usuario ya existe.")
                        if not mail_uni(email):
                            messagebox.showerror("Error", "El correo ya está en uso.")
                else:
                    messagebox.showerror("Error", "Las contraseñas no coinciden.")
            else:
                messagebox.showerror("Error", "La contraseña debe tener al menos 8 caracteres, una mayúscula, un número y un símbolo.")
        else:
            messagebox.showerror("Error", "Las contraseñas no coinciden.")
          
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
    def textot_cuadros(event):
        if telf_usu.get() == "Telefono": 
            telf_usu.delete(0, tk.END)
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
    telf_usu = tk.Entry(Ven_Prin, width=50, validate="key")
    telf_usu.config(validate="key", validatecommand=(Ven_Prin.register(val_num), "%P"))
    dpi_usu = tk.Entry(Ven_Prin, width=50, validate="key")
    dpi_usu.config(validate="key", validatecommand=(Ven_Prin.register(val_num), "%P"))
    contra_usu = tk.Entry(Ven_Prin, width=50, show="*")
    Conf_contra_usu = tk.Entry(Ven_Prin, width=50, show="*")

    #Texto en los cuadros.
    nom_usu.insert(0, "Nombre y Apellido") #con .insert agregamos el texto desde una posición inicial 0
    nickname_usu.insert(0, "Nombre de Usuario")
    email_usu.insert(0, "E-mail")
    telf_usu.insert(0, "Telefono")
    dpi_usu.insert(0, "DPI")

    #Labels.
    fuente_Titulo = ("Bahnschrift", 20) #Asigno una variable con el nombre y tamaño de la fuente.
    CrearCuenta_label = tk.Label(Ven_Prin, text="Crear Nueva Cuenta ", bg="white", font=fuente_Titulo) #Label se refiere a información o cuadros descriptivos. Con tk.Label agrego el texto descriptivo. Con bg le agrego color al fondo.

    #Fecha de Nacimiento.
    ven_fecha = None #Asigno ven fecha como variable global
    #Funciones para Fecha.
    def sel_fecha(): #Empezamos definiendo funciones
        global ven_fecha #menciono que es global y esa estoy usando.
        ven_fecha = tk.Toplevel(Ven_Prin) #tk.Toplevel me crea una nueva pestaña en donde pondré los selectores
        ven_fecha.title("Selector de Fecha") #Le doy un titulo.
        
        #Configuración de la Pestaña de Fecha.
        ancho_Ven_fecha = 320 
        alto_Ven_fecha = 240

        ancho_pantalla = Ven_Prin.winfo_screenwidth() 
        alto_pantalla = Ven_Prin.winfo_screenheight() 
        
        xf = (ancho_pantalla - ancho_Ven_fecha) // 2
        yf = (alto_pantalla - alto_Ven_fecha) // 2

        ven_fecha.geometry(f"{ancho_Ven_fecha}x{alto_Ven_fecha}+{xf}+{yf}") 

        ven_fecha.configure(bg="white") 

        marco = tk.Frame(ven_fecha) 
        marco.pack(pady=15)
        
        #Establezco variables.
        meses =["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
        dias = [str(i) for i in range(1,32)] #Uso un contador para sacar los días del 1 al 31.
        años = [str(i) for i in range(1990, 2025)]
        #Selectores.
        selec_mes = ttk.Combobox(ven_fecha, values=meses, state="readonly") #ttk.Combobox es para la barra selectora
        selec_dia = ttk.Combobox(ven_fecha, values=dias, state="readonly") #values le asigno valores.
        selec_año = ttk.Combobox(ven_fecha, values=años, state="readonly") #readonly es para que se seleccionen las opciones y no se pueda escribir en la barra.
        #Titulo.
        fuente_Titfecha = ("Bahnschrift", 16)
        fecha_label = tk.Label(ven_fecha, text="Ingresa Tu Fecha", bg="white", font=fuente_Titfecha)
        #Añadiré el botón de confirmación.
        B_confi = ttk.Button(ven_fecha, text="Confirmar Fecha", command=lambda: actual_fe(selec_mes, selec_dia, selec_año))
        #agregaré los selectores y el boton a la pestaña.
        fecha_label.pack(pady=5)
        selec_mes.pack(pady=5)
        selec_dia.pack(pady=5)
        selec_año.pack(pady=5)
        B_confi.pack(pady=5)
        
        def actual_fe(selec_mes, selec_dia, selec_año):#función para actualizar el boton.
                mes = selec_mes.get() #les asigno variables a los valores obtenidos
                dia = selec_dia.get()
                año = selec_año.get()
                fecha = f"{mes} {dia}, {año}" #introduzco como los voy a ordenar en fecha
                bot_fec.config(text=fecha) #Acá establezco la configuración, nuevo nombre, para el botón.
                ven_fecha.destroy() #Esto es para cerrar la ventana. 
    
    ruta_imagen = None            
    def cargar_foto():
        global ruta_imagen
        ruta_archivo = tkinter.filedialog.askopenfilename(filetypes=[("Imágenes", "*.png;*.jpg;*.jpeg")])
        if ruta_archivo:
            imagen = Image.open(ruta_archivo)
            imagen = imagen.resize((200, 200), Image.LANCZOS)  # Ajusta el tamaño de la imagen
            foto = ImageTk.PhotoImage(imagen)

            bot_foto.config(image=foto)
            bot_foto.image = foto
            ruta_imagen = ruta_archivo
            
    def guardar_foto():
        global nombre_archivo
        global ruta_imagen
        Usuario_N = nickname_usu.get()
        
        if ruta_imagen:
            nombre_archivo = f"imagen_{Usuario_N}.png" #acá crearé un nombre de imagen único
            ruta_destino = "C:\\Users\\danim\\OneDrive\\Documentos\\U\\Segundo Semetre\\Intro Progra\\Proyecto 0769\\Image_Users" #directorio de la imagen
            ruta_completa = os.path.join(ruta_destino, nombre_archivo) #Esto une 2 partes de una ruta de archivos

            imagen = Image.open(ruta_imagen)
            imagen.save(ruta_completa)
        else:
            messagebox.showerror("Error", "No se ha seleccionado ninguna imagen.")
            
    #Boton de guardado, fecha y mostrar.
    save_bot = tk.Button(Ven_Prin, text="Registrar", command=grab_regis, width=20) #Creo el boton con tk.Button, y le asigno la función que creé antes para guardar los datos ingresados. Con width configuro el largo.
    bot_fec = ttk.Button(Ven_Prin, text="Seleccionar Fecha de Nacimiento", width=50, command=sel_fecha)
    bot_mostrar = ttk.Button(Ven_Prin, image=mostrar_icon, command=bot_most_contra)
    bot_foto = ttk.Button(Ven_Prin, text="Cargar foto de perfil", width=50, command=cargar_foto)

    #Ahora coloco todo en la ventana.
    CrearCuenta_label.pack(padx=70, pady=(0, 5), anchor="w") #.pack hace que se ingresen uno debajo de otro.
    nom_usu.pack(padx=70, pady=(0, 5), anchor="w") #con "pady=" lo muevo por megapixeles en y o x "padx"
    nickname_usu.pack(padx=70, pady=(0, 5), anchor="w")
    email_usu.pack(padx=70, pady=(0, 5), anchor="w")
    telf_usu.pack(padx=70, pady=(0, 5), anchor="w")
    dpi_usu.pack(padx=70, pady=(0, 5), anchor="w")
    bot_foto.pack(padx=70, pady=(0, 5), anchor="w")
    bot_fec.pack(padx=70, pady=(0, 5), anchor="w")
    contra_usu.pack(padx=(70, 5), pady=(0, 5), anchor="w")
    bot_mostrar.pack(padx=210, pady=(0,5), anchor="w")
    Conf_contra_usu.pack(padx=70, pady=(0, 5), anchor="w")
    save_bot.pack(padx=70, pady=(30, 0), anchor="w")

    #Clicks
    #Relacionar función de borrar textos con los cuadros.
    nom_usu.bind("<Button-1>", texton_cuadros) #nombre es el a la variable que quiero asociar, .bind sirve para asociar eventos.
    nickname_usu.bind("<Button-1>", textoNn_cuadros)
    email_usu.bind("<Button-1>", textoe_cuadros) #<Button-1> representa el click izquierdo seguido de la función que a la que se le busca asociar.
    telf_usu.bind("<Button-1>", textot_cuadros)
    dpi_usu.bind("<Button-1>", textod_cuadros)

#FUnción para Inicio de Sesión.
#Funciones para Ventanas.
#Ventana Alumno
def ventana_alumno():
    subprocess.Popen(["python", "Estudiante.py"])
    Principal.quit()

#Ventana Administrador
def ventana_administrador():
    subprocess.Popen(["python", "p.py"])
    Principal.quit()
    
#Ventana Catedratico    
def ventana_catedratico():
    subprocess.Popen(["python", "Prof.py"])
    Principal.quit()

def detectar_y_reconocer_cara(img_capturada, ruta_imagen):
    messagebox.showinfo("Instrucciones", "Coloca tu cara frente a la cámara\n para así poder escanearla")
    # Cargar el clasificador de detección facial
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    cap = cv2.VideoCapture(0)

    # Cargar la imagen del usuario
    imagen_usuario = cv2.imread(ruta_imagen)
    imagen_gris = cv2.cvtColor(imagen_usuario, cv2.COLOR_BGR2GRAY)

    # Detectar caras en la imagen del usuario
    caras_usuario = face_cascade.detectMultiScale(imagen_gris, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    if len(caras_usuario) == 0:
        # No se encontraron caras en la imagen del usuario
        return False

    # Leer la imagen capturada por la cámara
    while True:
        _, img_capturada = cap.read()
        gray = cv2.cvtColor(img_capturada, cv2.COLOR_BGR2GRAY)

        # Detectar caras en la imagen de la cámara
        caras_camara = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in caras_camara:
            cv2.rectangle(img_capturada, (x,y), (x+w, y+h), (255, 0, 0), 2)
            # Comparar las caras detectadas en la cámara con la cara del usuario
            for (ux, uy, uw, uh) in caras_usuario:
                if x < ux < x + w and y < uy < y + h:
                    cap.release()
                    cv2.destroyAllWindows()
                    return True
        cv2.imshow("img_capturada", img_capturada)
        k = cv2.waitKey(30)
        if k == 27:
            cap.release()
            cv2.destroyAllWindows()
            break
    cap.release()

img_capturada = None
intentos = 3 #Numero de intentos para el inicio de sesión.  
def iniciar_sesion():
    global intentos
    usu_ingresado = usuario.get() #obtenemos usuario y contraseña ingresados.
    contra_ingresada = contraseña.get() 
    
    with open("Data.txt", "r") as archivo: #Abrimos archivo en modo lectura y metemos todo en una lista.
        datos = archivo.readlines()
        
    ruta_imagen = None  # Inicializa la variable de la ruta de la imagen
    
    usu_encontrado = False #DAmos valor a la variable.
    tipo_cuenta = "" #Asignamos la variable.
    estado_cuenta = ""
        
    for i in range(len(datos)): #Con for recorremos todos los valores de la lista, poniendo un rango desde el inicio hasta el final.
        if "Tipo de Cuenta: " in datos[i]: #Buscamos la linea.
            tipo_cuenta = datos[i].strip().split("Tipo de Cuenta: ")[1]
        if "Estado de Cuenta: " in datos[i]:
            estado_cuenta = datos[i].strip().split("Estado de Cuenta: ")[1]
        if tipo_cuenta == "Catedratico":
            if datos[i].strip() == f"Nombre: {usu_ingresado}": #el strip elimina espacios en blanco, y acá comparamos los datos hasta encontrar E-mail, si es el caso existe el correo.
                for j in range(i, min(i + 7, len(datos))): #pasa lo mismo al buscar contraseña
                    if "Contrasena: " in datos[j]: #acá busca una cadena igual a contraseña.
                        contrasena_encriptada = datos[j].strip().split("Contrasena: ")[1] #acá lo extraemos
                        contra_ingresada_encriptada = hashlib.sha256(contra_ingresada.encode()).hexdigest()
                        if estado_cuenta == "Bloqueado":
                            messagebox.showerror("Cuenta Bloqueada", "Esta cuenta está bloqueada. No puedes iniciar sesión.")
                            return
                        if contrasena_encriptada == contra_ingresada_encriptada:
                            usu_encontrado = True #Esto indica que se encontró y cierra los bucles
                            break
                if usu_encontrado:
                    break
        else:
            if datos[i].strip() == f"Usuario: {usu_ingresado}": #el strip elimina espacios en blanco, y acá comparamos los datos hasta encontrar E-mail, si es el caso existe el correo.
                for j in range(i, min(i + 7, len(datos))): #pasa lo mismo al buscar contraseña
                    if "Contrasena: " in datos[j]: #acá busca una cadena igual a contraseña.
                        contrasena_encriptada = datos[j].strip().split("Contrasena: ")[1] #acá lo extraemos
                        contra_ingresada_encriptada = hashlib.sha256(contra_ingresada.encode()).hexdigest()
                        if estado_cuenta == "Bloqueado":
                            messagebox.showerror("Cuenta Bloqueada", "Esta cuenta está bloqueada. No puedes iniciar sesión.")
                            return
                        if contrasena_encriptada == contra_ingresada_encriptada:
                            usu_encontrado = True #Esto indica que se encontró y cierra los bucles
                            break
                if usu_encontrado:
                    break
        
    if usu_encontrado:
        #Agregamos de que tipo de cuenta se abrira.
        if tipo_cuenta == "Alumno":
            for i in range(len(datos)):
                if datos[i].strip().startswith("Usuario: " + usu_ingresado):
                    # Encuentra la línea con la información del usuario
                    for j in range(i, min(i + 7, len(datos))):
                        if datos[j].strip().startswith("Imagen: "):
                            ruta_imagen = datos[j].split("Imagen: ")[1].strip()
                            break

            if ruta_imagen is not None:
                # Verificar la cara del usuario llamando la función del módulo "RECO"
                if not detectar_y_reconocer_cara(img_capturada, ruta_imagen):
                    messagebox.showerror("Error", "La cara del usuario no coincide. Intente nuevamente.")
                    return
            else:
                # No se encontró la ruta de la imagen del usuario en los datos
                messagebox.showerror("Error", "Usuario no encontrado o información incompleta.")
                return
            messagebox.showinfo("Inicio de Sesión", "¡Inicio de sesión exitoso!")
            ventana_alumno()
            
        elif tipo_cuenta == "Administrador":
                messagebox.showinfo("Inicio de Sesión", "¡Inicio de sesión exitoso!")
                ventana_administrador()
        elif tipo_cuenta == "Catedratico":
                messagebox.showinfo("Inicio de Sesión", "¡Inicio de sesión exitoso!")
                ventana_catedratico()
    else:
        intentos -= 1
        if intentos == 0:
            messagebox.showerror("Cuenta Bloqueada", "Has excedido el número de intentos.")
            #Cambiaré el estado de Bloqueado a desbloqueado.
            cambiar_estado_cuenta("Desbloqueado", "Bloqueado")
            
        else:
            messagebox.showerror("Error", f"El usuario o la contraseña son incorrectos. Intentos: {intentos}")

def cambiar_estado_cuenta(estado_actual, estado_nuevo):
    with open("Data.txt", "r") as archivo:
        datos = archivo.readlines()
    with open("Data.txt", "w") as archivo:
        for linea in datos:
            if f"Estado de Cuenta: {estado_actual}" in linea:
                linea = linea.replace(estado_actual, estado_nuevo)
            archivo.write(linea)

def bot_most_contra(): #defino la variable. cget selecciona un valor establecido de una variable para poder trabajar en él.
        if contraseña.cget("show") == "*": #Acá se verifica si el contenido es "*", ósea, esta oculta.
            contraseña.config(show="") #Esto genera el cambio de "*" a una cadena vacía, haría que se muestre la contra.
            bot_mostrar.config(image = mostrar_icon) #Esto hace que se muestre la imagen.
        else: 
            contraseña.config(show="*") #Si la contra no era "*" significa que se ve, por lo que esto lo cambia "*".
            bot_mostrar.config(image = ocultar_icon)


#LOGO
Logo_icon = tk.PhotoImage(file="USAC_Logo.png") #Las cargo con tk.Photo, de la carpeta.

#LABELS
fuente_Titulo = ("Bahnschrift", 20) #Asigno una variable con el nombre y tamaño de la fuente.
Logo_label = tk.Label(Principal, image=Logo_icon, bg="white")
Inicio_label = tk.Label(Principal, text="Inicio de Sesión", bg="white", font=fuente_Titulo) #Label se refiere a información o cuadros descriptivos. Con tk.Label agrego el texto descriptivo. Con bg le agrego color al fondo.
Usario_label = tk.Label(Principal, text="Usuario:", bg="white")
Contraseña_label = tk.Label(Principal, text="Contraseña:", bg="white")
recu_contra_label = tk.Label(Principal, text="¿Tienes algún problema?", bg="white", fg="blue", cursor="hand2") #Acá cursor solo cambia el aspecto del mouse al pasar por esto.

espacio_label = tk.Label(Principal, text=" ", width=50, bg="white")

#BOTONES
Iniciar = tk.Button(Principal, text="Iniciar", width=20, command=iniciar_sesion)
Registrar = tk.Button(Principal, text="Registrar", width=20, command=registrar)
bot_mostrar = ttk.Button(Principal, image=mostrar_icon, command=bot_most_contra)

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
recu_contra_label.pack(padx=(170, 0))
bot_mostrar.pack()
espacio_label.pack(side="left")
Iniciar.pack(side="left", padx=10)
Registrar.pack(side="left")

#CLICKS
recu_contra_label.bind("<Button-1>", lambda event: contra_olvid())

Principal.mainloop()