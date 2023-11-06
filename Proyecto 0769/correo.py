import os #para variables de entorno
from dotenv import load_dotenv
from email.message import EmailMessage #para el correo
import ssl #para mandarlo de forma segura.
import smtplib

load_dotenv()
#Variables con los datos del remitente y el receptor.
email_sender = "edusac446@gmail.com"
Password = os.getenv("PASSWORD") #La contraseña que con la libreria os la extraemos del archivo .env (como variable de entorno)
email_reciver = "danimarroquin.1@gmail.com"
#Subject=asunto    Body=cuerpo
subject = "Recuperación de contraseña"
body = "Tu contraseña es"
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