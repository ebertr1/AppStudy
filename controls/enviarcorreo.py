import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

CORREO_ELECTRONICO = "isabel.morocho@unl.edu.ec"
CONTRASENIA = "ycqcfomvocqvtbax"

# Conexión con el servidor 
with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    
    smtp.login(CORREO_ELECTRONICO, CONTRASENIA)
    
    destinatarios = ["isabelkaty07@gmail.com", "isabel.morocho@unl.edu.ec"]
    asunto = "Notificación de Bajo Rendimiento Académico"
    
    # Crear el contenedor del mensaje en formato multipart
    mensaje = MIMEMultipart()
    mensaje['From'] = CORREO_ELECTRONICO
    mensaje['To'] = ", ".join(destinatarios)
    mensaje['Subject'] = asunto
    
    # Crear el cuerpo del mensaje en HTML
    cuerpo_html = """
    <html>
        <body>
            <h1>Notificación de Bajo Rendimiento Académico</h1>
            <p>Estimado/a estudiante,</p>
            <p>Nos dirigimos a usted para informarle que su rendimiento académico no ha alcanzado los estándares requeridos.</p>
            <p>Entendemos que esta situación puede ser preocupante, pero queremos ofrecerle nuestro apoyo para ayudarle a mejorar su desempeño.</p>
            <p>Le recomendamos que aproveche los siguientes recursos:</p>
            <ul>
                <li>Asesorías académicas disponibles en el centro de tutoría por los docentes en el cubiculo.</li>
                <li>Recursos Académicos brindados por los docentes</li>
                
            </ul>
            <p>Atentamente,</p>
            <p>El equipo académico</p>
            <p>Ingeniería en las Ciencias de la Computación</p>
        <div style="display: flex; gap: 20px;">
    <img src="https://univercimas.com/wp-content/uploads/2021/04/Universidad-Nacional-de-Loja-UNL-300x300.png" alt="Universidad" style="width:200px;height:auto;">
    </div>
        <p><i>Educamos para Transformar</i></p>


        </body>
    </html>
    """
    
    # Adjuntar el cuerpo HTML al mensaje
    mensaje.attach(MIMEText(cuerpo_html, 'html'))
    
    # Enviar el correo
    smtp.sendmail(CORREO_ELECTRONICO, destinatarios, mensaje.as_string())
    
    
    #ESTE SCRIPT SOLO FUNCIONA CON MI CORREO, SI DESEA PROBARLO CON OTRO CORREO DEBE HABILITAR EL ACCESO A APLICACIONES Y ACCEEDER A CLAVE DE APLICACIONES
