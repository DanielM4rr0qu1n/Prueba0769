import tkinter as tk #Le doy un alias a la biblioteca
from tkinter import ttk #Importo ttk para mejores widgets
from tkinter import messagebox #Con esto importo las pestañas emergentes de mensajes y avisos.
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import re
import hashlib

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

mostrar_icon = tk.PhotoImage(file="Mostrar.png") #Las cargo con tk.Photo, de la carpeta.
ocultar_icon = tk.PhotoImage(file="Oculto.png")

#Empiezan Funcionamientos
#Funciones
mail_recu = None
def contra_olvid():
    global mail_recu
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
    
    #Funciones
    def enviar_correo(destinatario, asunto, mensaje):
        # Configura tus credenciales de correo saliente (SMTP)
        remitente_email = "Yrobles282002@gmail.com"  # Tu dirección de correo
        remitente_password = "------"  # Tu contraseña

        # Configura el servidor SMTP
        smtp_server = "smtp.gmail.com"  # Puedes cambiarlo según tu proveedor de correo
        smtp_port = 587  # Puerto de SMTP

        # Crear un objeto SMTP
        server = smtplib.SMTP(smtp_server, smtp_port)

        # Iniciar la conexión con el servidor
        server.starttls()

        # Iniciar sesión en tu cuenta de correo
        server.login(remitente_email, remitente_password)

        # Crear el mensaje
        msg = MIMEMultipart()
        msg["From"] = remitente_email
        msg["To"] = destinatario
        msg["Subject"] = asunto

        # Agregar el mensaje al cuerpo
        msg.attach(MIMEText(mensaje, "plain"))

        # Enviar el correo
        server.sendmail(remitente_email, destinatario, msg.as_string())

        # Cerrar la conexión
        server.quit()
    
    def recuperar_contrasena():
        correo = mail_recu.get() #variable para el correo ingresado
        with open("Data.txt", "r") as archivo: #abro el txt en lectura
            datos = archivo.readlines() #Lee todas las lineas de un archivo y las mete en una lista.

        usuario_encontrado = False #Valores a variables
        contrasena = None

        for i in range(len(datos)): #Con for recorremos todos los valores de la lista, poniendo un rango desde el inicio hasta el final.
            if datos[i].strip() == f"E-mail: {correo}": #el strip elimina espacios en blanco, y acá comparamos los datos hasta encontrar E-mail, si es el caso existe el correo.
                for j in range(i, min(i + 7, len(datos))): #pasa lo mismo al buscar contraseña
                    if "Contrasena: " in datos[j]: #acá busca una cadena igual a contraseña.
                        contrasena = datos[j].strip().split("Contrasena: ")[1] #acá lo extraemos
                usuario_encontrado = True #Esto indica que se encontró y cierra los bucles
                break

        if usuario_encontrado and contrasena:
            asunto = "Recuperación de contraseña"
            mensaje = f"Tu contraseña es: {contrasena}"
            enviar_correo(correo, asunto, mensaje)
            messagebox.showinfo("Recuperar Contraseña", "La contraseña ha sido enviada a tu correo.")
        else:
            messagebox.showerror("Error", "El correo no se encontró en la base de datos.")

    
    #WIDGETS
    #Labels
    tit_fuent = ("Bahnschrift", 14)
    tit_label = tk.Label(Recuperar, text="Recuperar contraseña", bg="papayawhip", font=tit_fuent)
    info_label = tk.Label(Recuperar, text="Ingresa tu correo y luego se te mandará\n un correo con tu contraseña dentro.", bg="papayawhip")
    recu_label = tk.Label(Recuperar, text="E-mail:", bg="papayawhip")
    
    #Cuadros de Texto
    mail_recu = tk.Entry(Recuperar, width=50)
    
    #Botones
    send_mail = tk.Button(Recuperar, text="Enviar", command=recuperar_contrasena)
    
    #PACKS
    tit_label.pack(pady=(30, 5))
    info_label.pack(pady=(0, 5))
    recu_label.pack(pady=(0, 5))
    mail_recu.pack(pady=(0, 5))
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
    Ven_Prin.configure(bg="papayawhip") #.config da varias opciones para modificar cosas como estetica, bg es para colores.

    #Agrego un margen.
    marco = tk.Frame(Ven_Prin) #Con tk.Frame añade el marco.
    marco.pack(pady=70) #Añado el margen y le doy valores.

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
    def guard_data(nombres, usuario, email, telf, dpi, fecha, contraseña):
        with open("Data.txt", "a") as archivo: #open abre el archivo, "a" es para agregar.
            
            #Encriptar contra
            contraseña_encriptada = hashlib.sha256(contraseña.encode()).hexdigest()
            
            archivo.write(f"Tipo de Cuenta: Alumno\n")
            archivo.write(f"Nombre: {nombres}\n")
            archivo.write(f"Usuario: {usuario}\n")
            archivo.write(f"E-mail: {email}\n")
            archivo.write(f"Telefono: {telf}\n")
            archivo.write(f"DPI: {dpi}\n")
            archivo.write(f"Fecha de Nacimiento: {fecha}\n")
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
        
    def grab_regis(): #acá creo una función la cuál usaré para darle sentido al botón de "registrar"
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
                        guard_data(nombres, usuario, email, telf, dpi, fecha, contraseña)
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
    CrearCuenta_label = tk.Label(Ven_Prin, text="Crear Nueva Cuenta ", bg="papayawhip", font=fuente_Titulo) #Label se refiere a información o cuadros descriptivos. Con tk.Label agrego el texto descriptivo. Con bg le agrego color al fondo.

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

        ven_fecha.configure(bg="papayawhip") 

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
        fecha_label = tk.Label(ven_fecha, text="Ingresa Tu Fecha", bg="papayawhip", font=fuente_Titfecha)
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
        
    #Boton de guardado, fecha y mostrar.
    save_bot = tk.Button(Ven_Prin, text="Registrar", command=grab_regis, width=20) #Creo el boton con tk.Button, y le asigno la función que creé antes para guardar los datos ingresados. Con width configuro el largo.
    bot_fec = ttk.Button(Ven_Prin, text="Seleccionar Fecha de Nacimiento", width=50, command=sel_fecha)
    bot_mostrar = ttk.Button(Ven_Prin, image=mostrar_icon, command=bot_most_contra)

    #Ahora coloco todo en la ventana.
    CrearCuenta_label.pack(padx=70, pady=(0, 5), anchor="w") #.pack hace que se ingresen uno debajo de otro.
    nom_usu.pack(padx=70, pady=(0, 5), anchor="w") #con "pady=" lo muevo por megapixeles en y o x "padx"
    nickname_usu.pack(padx=70, pady=(0, 5), anchor="w")
    email_usu.pack(padx=70, pady=(0, 5), anchor="w")
    telf_usu.pack(padx=70, pady=(0, 5), anchor="w")
    dpi_usu.pack(padx=70, pady=(0, 5), anchor="w")
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
def ventana_alumno():
    # Función para agregar cursos desde el archivo de texto
    def agregar_curso(nombre, descripcion):
        with open("cursos.txt", "a") as file:
            file.write(f"{nombre}\n{descripcion}\n\n")

    # Función para cargar cursos desde el archivo de texto
    def cargar_cursos_disponibles():
        cursos = []
        with open("cursos.txt", "r") as file:
            course_info = []
            for line in file:
                line = line.strip()  # Eliminar espacios en blanco al principio y al final
                if line:  # Verificar si la línea no está vacía
                    course_info.append(line)
                else:
                    if len(course_info) == 2:  # Comprobar si se han recopilado dos líneas (nombre y descripción)
                        nombre, descripcion = course_info
                        cursos.append((nombre, descripcion))
                    course_info = []
        return cursos
        
    # Función para asignarse a un curso
    def asignarse_a_curso(curso_id):
        cursos_asignados.append(curso_id)
        messagebox.showinfo("Asignación", f"¡Te has asignado al curso {curso_id}!")

    # Función para mostrar la ventana de cursos asignados
    def mostrar_cursos_asignados():
        ventana_cursos_asignados = tk.Toplevel()
        ventana_cursos_asignados.title("Cursos Asignados")
        ventana_cursos_asignados.configure(bg="papayawhip")
        
        ancho_VenEstu = 640 # Pongo el tamaño que busco de la ventana
        alto_VenEstu = 340

        ancho_pantalla = ventana_cursos_asignados.winfo_screenwidth() #Obtengo el ancho y alto de la pantalla con la información
        alto_pantalla = ventana_cursos_asignados.winfo_screenheight() #Con .winfo encuentro la información de la pantalla en la que trabajo

        x = (ancho_pantalla - ancho_VenEstu) // 2 #Calculo la posición para centrar la ventana en la pantalla
        y = (alto_pantalla - alto_VenEstu) // 2 #Esto va en relación a los bordes al rededor de la ventana, de ahí la fórmula

        ventana_cursos_asignados.geometry(f"{ancho_VenEstu}x{alto_VenEstu}+{x}+{y}")

        for curso_id in cursos_asignados:
            curso_info = cursos_disponibles[curso_id - 1]
            curso_nombre, curso_descripcion = curso_info
            label = tk.Label(ventana_cursos_asignados, text=f"Curso: {curso_nombre}", font=("Arial", 12), bg="papayawhip")
            label.pack()
            descripcion_label = tk.Label(ventana_cursos_asignados, text=f"Descripción: {curso_descripcion}", font=("Arial", 10), bg="papayawhip")
            descripcion_label.pack()

    # Crear ventana de estudiante
    #Ventana de Asignaciones
    def ventana_estudiante():
        ventana_est = tk.Toplevel()
        ventana_est.title("Asignaciones")
        ventana_est.configure(bg="papayawhip")
        
        ancho_est = 640 # Pongo el tamaño que busco de la ventana
        alto_est = 340

        ancho_pantalla = ventana_est.winfo_screenwidth() #Obtengo el ancho y alto de la pantalla con la información
        alto_pantalla = ventana_est.winfo_screenheight() #Con .winfo encuentro la información de la pantalla en la que trabajo

        x = (ancho_pantalla - ancho_est) // 2 #Calculo la posición para centrar la ventana en la pantalla
        y = (alto_pantalla - alto_est) // 2 #Esto va en relación a los bordes al rededor de la ventana, de ahí la fórmula

        ventana_est.geometry(f"{ancho_est}x{alto_est}+{x}+{y}")

        for i, curso_info in enumerate(cursos_disponibles):
            curso_nombre, _ = curso_info
            curso_button = tk.Button(ventana_est, text=f"Curso: {curso_nombre}", command=lambda id=i + 1: asignarse_a_curso(id))
            curso_button.pack()

    # Configuración de la ventana principal
    ventana_principal = tk.Tk()
    ventana_principal.title("Cursos en Línea")
    ventana_principal.configure(bg="papayawhip")
    
    ancho_VenEstu = 1040 # Pongo el tamaño que busco de la ventana
    alto_VenEstu = 640

    ancho_pantalla = ventana_principal.winfo_screenwidth() #Obtengo el ancho y alto de la pantalla con la información
    alto_pantalla = ventana_principal.winfo_screenheight() #Con .winfo encuentro la información de la pantalla en la que trabajo

    x = (ancho_pantalla - ancho_VenEstu) // 2 #Calculo la posición para centrar la ventana en la pantalla
    y = (alto_pantalla - alto_VenEstu) // 2 #Esto va en relación a los bordes al rededor de la ventana, de ahí la fórmula

    ventana_principal.geometry(f"{ancho_VenEstu}x{alto_VenEstu}+{x}+{y}")

    cursos_asignados = []  # Lista para almacenar los cursos asignados
    cursos_disponibles = cargar_cursos_disponibles()

    # Barra superior con fondo azul
    barra_superior = tk.Frame(ventana_principal, bg="DeepSkyBlue2")
    barra_superior.pack(fill="x")
    
    #Funcion para Perfil.
    #Acá obtengo los datos para luego ponerlos en una varibble.
    def obtener_datos_estudiante():
        datos_estudiante = {}
        with open("Data.txt", "r") as archivo:
            datos = archivo.readlines()
            for i in range(len(datos)):
                if "Tipo de Cuenta: Alumno" in datos[i]:
                    for j in range(i, min(i + 7, len(datos))):
                        # Divide cada línea en campo y valor
                        campo, valor = datos[j].strip().split(": ", 1)
                        datos_estudiante[campo] = valor
        return datos_estudiante
    #Esta es la ventana que se abre que hará uso de los datos de estudiantes.
    def ventana_perfil():
        ventana_perfil = tk.Toplevel()
        ventana_perfil.title("Perfil del Estudiante")
        ventana_perfil.configure(bg="papayawhip")
        
        ancho_VenEstu = 440 # Pongo el tamaño que busco de la ventana
        alto_VenEstu = 240

        ancho_pantalla = ventana_perfil.winfo_screenwidth() #Obtengo el ancho y alto de la pantalla con la información
        alto_pantalla = ventana_perfil.winfo_screenheight() #Con .winfo encuentro la información de la pantalla en la que trabajo

        x = (ancho_pantalla - ancho_VenEstu) // 2 #Calculo la posición para centrar la ventana en la pantalla
        y = (alto_pantalla - alto_VenEstu) // 2 #Esto va en relación a los bordes al rededor de la ventana, de ahí la fórmula

        ventana_perfil.geometry(f"{ancho_VenEstu}x{alto_VenEstu}+{x}+{y}")

        datos_estudiante = obtener_datos_estudiante()

        for campo, valor in datos_estudiante.items():
            # Se excluye la contraseña
            if campo != "Contrasena":
                label = tk.Label(ventana_perfil, text=f"{campo}: {valor}", font=("Arial", 12), bg="papayawhip")
                label.pack()
    
    #Con esta función se saca el nombre correspondiente del txt
    def obtener_nombre_estudiante():
        with open("Data.txt", "r") as archivo:
            datos = archivo.readlines()

        for i in range(len(datos)):
            if "Tipo de Cuenta: Alumno" in datos[i]:
                for j in range(i, min(i + 7, len(datos))):
                    if "Nombre: " in datos[j]:
                        return datos[j].strip().split("Nombre: ")[1]
        return "Estudiante Desconocido"

    # Obtener el nombre del usuario
    nombre_usuario = obtener_nombre_estudiante()

    # Etiqueta para mostrar el nombre de usuario
    usuario_label = tk.Label(barra_superior, text=f"Bienvenido, {nombre_usuario}", font=("Arial", 12), bg="DeepSkyBlue2", fg="white", cursor="hand2")
    usuario_label.pack(side="right", padx=10, pady=10)
    usuario_label.bind("<Button-1>", lambda event: ventana_perfil())
    
    # Margen en blanco en la parte superior
    margen_superior = tk.Frame(ventana_principal, bg="papayawhip", height=20)
    margen_superior.pack(fill="x")

    # Botón "Mis cursos"
    mis_cursos_button = tk.Button(ventana_principal, text="Mis cursos", font=("Arial", 14), bg="DeepSkyBlue2", fg="white", command=mostrar_cursos_asignados)
    mis_cursos_button.pack(pady=10)

    # Margen en blanco en la parte media
    margen_medio = tk.Frame(ventana_principal, bg="papayawhip", height=20)
    margen_medio.pack(fill="x")

    # Crear mosaicos
    mosaicos_frame = tk.Frame(ventana_principal, bg="papayawhip")
    mosaicos_frame.pack()

    # Lista de nombres de mosaico
    nombres_mosaico = [
        "Asignaciones",
        "Notas",
        "Desasignaciones"
    ]

    # Lista de descripciones de mosaicos
    descripcion_mosaicos = [
        "Asignarse a cursos disponibles.",
        "Notas presentes en los cursos.",
        "Podras eliminar los cursos que ya no quieras seguir."
    ]

    # Tamaño de imagen de mosaico
    tamaño_imagen_mosaico = (150, 150)

    # Crear mosaicos
    for i in range(len(nombres_mosaico)):
        mosaico = ttk.Frame(mosaicos_frame, padding=10)
        mosaico.grid(row=i // 3, column=i % 3, padx=20, pady=10)

        nombres_mosaico_label = tk.Label(mosaico, text=nombres_mosaico[i], font=("Arial", 12), bg="papayawhip", fg="DeepSkyBlue2")
        nombres_mosaico_label.pack()

        descripcion_mosaico_label = tk.Label(mosaico, text=descripcion_mosaicos[i], font=("Arial", 10), bg="papayawhip", fg="DeepSkyBlue2")
        descripcion_mosaico_label.pack()

        if i == 0:  # Si es el primer mosaico (Asignaciones)
            boton_mosaico = tk.Button(mosaico, text=f"Ir a {nombres_mosaico[i]}", font=("Arial", 10), bg="DeepSkyBlue2", fg="white", command=ventana_estudiante)
        else:
            boton_mosaico = tk.Button(mosaico, text=f"Ir a {nombres_mosaico[i]}", font=("Arial", 10), bg="DeepSkyBlue2", fg="white")

        boton_mosaico.pack()
        
#Ventana Administrador
def ventana_administrador():
    
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
                file.write(f"Tipo de Cuenta: Catedratico\n")
                file.write(f"Usuario: {nombre}\n")
                file.write(f"Apellido: {apellido}\n")
                file.write(f"DPI: {dpi}\n")
                file.write(f"Contrasena: {password_hash}\n")
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

    
    window = tk.Toplevel()
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
    
def ventana_catedratico():
    # Crea una ventana de Tkinter
    window = tk.Toplevel()
    
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
    
def iniciar_sesion():
    usu_ingresado = usuario.get() #obtenemos usuario y contraseña ingresados.
    contra_ingresada = contraseña.get()
    
    with open("Data.txt", "r") as archivo: #Abrimos archivo en modo lectura y metemos todo en una lista.
        datos = archivo.readlines()
        
        usu_encontrado = False #DAmos valor a la variable.
        tipo_cuenta = "" #Asignamos la variable.
        
    for i in range(len(datos)): #Con for recorremos todos los valores de la lista, poniendo un rango desde el inicio hasta el final.
        if "Tipo de Cuenta: " in datos[i]: #Buscamos la linea.
            tipo_cuenta = datos[i].strip().split("Tipo de Cuenta: ")[1]
        if datos[i].strip() == f"Usuario: {usu_ingresado}": #el strip elimina espacios en blanco, y acá comparamos los datos hasta encontrar E-mail, si es el caso existe el correo.
            for j in range(i, min(i + 7, len(datos))): #pasa lo mismo al buscar contraseña
                if "Contrasena: " in datos[j]: #acá busca una cadena igual a contraseña.
                    contrasena_encriptada = datos[j].strip().split("Contrasena: ")[1] #acá lo extraemos
                    contra_ingresada_encriptada = hashlib.sha256(contra_ingresada.encode()).hexdigest()
                    if contrasena_encriptada == contra_ingresada_encriptada:
                        usu_encontrado = True #Esto indica que se encontró y cierra los bucles
                        break
            if usu_encontrado:
                break
            
    if usu_encontrado:
        messagebox.showinfo("Inicio de Sesión", "¡Inicio de sesión exitoso!")
        
        #Agregamos de que tipo de cuenta se abrira.
        if tipo_cuenta == "Alumno":
                ventana_alumno()
        elif tipo_cuenta == "Administrador":
                ventana_administrador()
        elif tipo_cuenta == "Catedratico":
                ventana_catedratico()
    else:
        messagebox.showerror("Error", "El usuario o la contraseña son incorrectos.")

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
Logo_label = tk.Label(Principal, image=Logo_icon, bg="papayawhip")
Inicio_label = tk.Label(Principal, text="Inicio de Sesión", bg="papayawhip", font=fuente_Titulo) #Label se refiere a información o cuadros descriptivos. Con tk.Label agrego el texto descriptivo. Con bg le agrego color al fondo.
Usario_label = tk.Label(Principal, text="Usuario:", bg="papayawhip")
Contraseña_label = tk.Label(Principal, text="Contraseña:", bg="papayawhip")
recu_contra_label = tk.Label(Principal, text="¿Has olvidado tu contraseña?", bg="papayawhip", fg="blue", cursor="hand2") #Acá cursor solo cambia el aspecto del mouse al pasar por esto.

espacio_label = tk.Label(Principal, text=" ", width=50, bg="papayawhip")

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
recu_contra_label.pack(padx=(150, 0))
bot_mostrar.pack()
espacio_label.pack(side="left")
Iniciar.pack(side="left", padx=10)
Registrar.pack(side="left")

#CLICKS
recu_contra_label.bind("<Button-1>", lambda event: contra_olvid())

Principal.mainloop()

